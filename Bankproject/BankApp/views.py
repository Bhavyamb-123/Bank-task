from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import*
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .models import Profile

# Home Page
def homepage(request):
    return render(request, 'home.html')
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

