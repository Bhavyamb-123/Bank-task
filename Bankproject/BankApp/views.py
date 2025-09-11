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

def loan(request):
    return render(request,'loan.html') 

def personalloanapplication(request):
    return render(request,'personalloanapplication.html')

def educationloanapplication(request):
    return render(request,'educationloanapplication.html')

def homeloan(request):
    return render(request,'homeloan.html')  


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

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import LoanApplication

def home_loan_application(request):
    if request.method == "POST":
        loan_app = LoanApplication.objects.create(
            loan_amount=request.POST.get("loanAmount"),
            loan_purpose=request.POST.get("loanPurpose"),
            property_type=request.POST.get("propertyType"),
            down_payment=request.POST.get("downPayment"),

            first_name=request.POST.get("firstName"),
            last_name=request.POST.get("lastName"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            date_of_birth=request.POST.get("dateOfBirth"),
            marital_status=request.POST.get("maritalStatus"),
            current_address=request.POST.get("currentAddress"),

            employment_type=request.POST.get("employmentType"),
            monthly_income=request.POST.get("monthlyIncome"),
            work_experience=request.POST.get("workExperience"),
            company_name=request.POST.get("companyName"),
            existing_loans=request.POST.get("existingLoans") or None,
            credit_score=request.POST.get("creditScore") or None,

            property_value=request.POST.get("propertyValue"),
            property_age=request.POST.get("propertyAge"),
            property_city=request.POST.get("propertyCity"),
            property_area=request.POST.get("propertyArea"),
            property_address=request.POST.get("propertyAddress"),

            agree_terms=True if request.POST.get("agreeTerms") else False,
            credit_check=True if request.POST.get("creditCheck") else False
        )
        return HttpResponse("✅ Application submitted successfully! We will contact you within 24 hours.")
    
    return render(request, "loanapplication.html") 