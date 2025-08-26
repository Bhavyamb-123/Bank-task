from django.shortcuts import render
from django.contrib.auth.models import User
from.models import *
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def homepage(request):
    return render(request,'home.html')
<<<<<<< HEAD
=======

def signup(request):
    if request.method=="POST":
        user=User.objects.create(username=request.POST.get("email"))
        user.set_password(request.POST.get("password"))
        user.save()
        Profile.objects.create(
            user=user,
            Firstname=request.POST.get("firstname"),
            Lastname=request.POST.get("lastname"),
            Email=request.POST.get("email"),
            Phonenumber=request.POST.get("number"),
            Pin=request.POST.get("pin"),
            )
        return HttpResponseRedirect(reverse("homepage"))

def userlogin(request):
    msg=""
    if request.method=="POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user=authenticate(username=username,password=password)  #for authentication .value will be true or false
        if user:
            login(request,user)
            print("login successful")
            return HttpResponseRedirect(reverse("homepage"))
        else:
            print("No such user found")
            msg="invalid login credentials"
        print(username,password)
    return render(request,'home.html',{'msg':msg})

def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse("homepage"))
>>>>>>> b765fde6881edb1815186bf9d8ef80923574da71
