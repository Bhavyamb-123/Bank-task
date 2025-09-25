from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import*
from django.http import HttpResponseRedirect,JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse




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
        # Save application details
        app = AccountApplication.objects.create(
            account_type=request.POST.get("accountType"),
            first_name=request.POST.get("firstName"),
            last_name=request.POST.get("lastName"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            date_of_birth=request.POST.get("dateOfBirth"),
            ssn=request.POST.get("ssn"),
            address=request.POST.get("address"),
            city=request.POST.get("city"),
            state=request.POST.get("state"),
            zip_code=request.POST.get("zipCode"),
            employment=request.POST.get("employment"),
            income=request.POST.get("income"),
            pet_name=request.POST.get("petName"),
            birth_city=request.POST.get("birthCity"),
            initial_deposit=request.POST.get("initialDeposit") or 0.00,
            terms_accepted=bool(request.POST.get("terms")),
            marketing_opt_in=bool(request.POST.get("marketing")),
            document_upload=request.FILES.get("documentUpload"),
        )

        # If AJAX request → return JSON
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            return JsonResponse({
                "success": True,
                "message": "Application submitted successfully!"
            })
        
        # Otherwise redirect to homepage with success message
        return redirect(reverse('homepage'))

    # For GET requests → show the account opening page
    return render(request, "openacc.html")


# ===== DEBIT CARD =====
def debit_card_page(request):
    return render(request, "debitcard.html")


def apply_debitcard(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        email = request.POST.get("email")
        account_number = request.POST.get("account_number")
        cardType = request.POST.get("cardType")

        DebitCardApplication.objects.create(
            user=request.user if request.user.is_authenticated else None,
            fullname=fullname,
            email=email,
            account_number=account_number,
            cardType=cardType,
        )
        messages.success(request, "✅ Your debit card application has been submitted successfully!")
        return redirect("debitcard")
        #print
    return render( request, "debitcard.html")
