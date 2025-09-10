from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import*
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Profile

# Home Page
def homepage(request):
    return render(request,'home.html')

def openacc(request):
    return render(request,'openacc.html') 

users = User.objects.all()
# for u in users:
#     if u.username != "admin":
#         u.delete()
# Signup View
def signup(request):
    msg = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        print("------------",password)
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        number = request.POST.get("number")
        pin = request.POST.get("pin")

        # Check if user already exists
        if User.objects.filter(username=email).exists():
            msg = "User with this email already exists."
            return render(request, 'home.html', {'msg': msg})

        # Create User
        user = User.objects.create(username=email, email=email, password=password)
        user.set_password(password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()

        # Create Profile
        Profile.objects.create(
            user=user,
            Firstname=firstname,
            Lastname=lastname,
            Email=email,
            Phonenumber=number,
            Pin=pin,
        )

        # Automatically log in the user
        login(request, user)
        return redirect("homepage")

    return render(request, 'home.html', {'msg': msg})

# Login View
def userlogin(request):
    msg = ""
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        # Authenticate user
        user = authenticate(username=email, password=password)
        print(user)
        if user is not None:
            print("----------------")
            login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            msg = "Invalid login credentials"
    

    return HttpResponseRedirect(reverse('homepage'))

# Logout View
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))



def open_account(request):
    if request.method == "POST":
        # Step 1: Account Type
        account_type = request.POST.get("account_type")

        # Step 2: Personal Info (HTML names kept as-is)
        dob = request.POST.get("dateOfBirth")   # HTML: dateOfBirth
        ssn = request.POST.get("ssn")           # HTML: ssn
        address = request.POST.get("address")   # HTML: address
        city = request.POST.get("city")         # HTML: city
        state = request.POST.get("state")       # HTML: state
        zipcode = request.POST.get("zipCode")   # HTML: zipCode
        employment = request.POST.get("employment")  # HTML: employment
        income = request.POST.get("income")          # HTML: income

        # Step 3: Identity Verification
        document = request.FILES.get("idDocument")  # HTML: idDocument
        security_q1 = request.POST.get("securityQuestion1")  # HTML: securityQuestion1
        security_q2 = request.POST.get("securityQuestion2")  # HTML: securityQuestion2

        # Step 4: Review & Deposit
        initial_deposit = request.POST.get("initialDeposit") or 0  # HTML: initialDeposit
        agree_terms = request.POST.get("agreeTerms") == "on"       # HTML: agreeTerms
        agree_marketing = request.POST.get("agreeMarketing") == "on"  # HTML: agreeMarketing

        # Get or create Profile of logged-in user
        profile = Profile.objects.filter(user=request.user).first()
        if not profile:
            profile = Profile.objects.create(
                user=request.user,
                Firstname=request.user.first_name,
                Lastname=request.user.last_name,
                Email=request.user.email
            )

        # Save AccountApplication
        AccountApplication.objects.create(
            profile=profile,
            account_type=account_type,
            date_of_birth=dob,
            ssn=ssn,
            address=address,
            city=city,
            state=state,
            zipcode=zipcode,
            employment_status=employment,
            annual_income=income,
            id_document=document,
            security_question1=security_q1,
            security_question2=security_q2,
            initial_deposit=initial_deposit,
            agree_terms=agree_terms,
            agree_marketing=agree_marketing,
        )

        return redirect("account_success")

    return render(request, "open_account/form.html")



def account_success(request):
    return render(request, "open_account/success.html")



