# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from .models import*
# from django.http import HttpResponseRedirect
# from django.contrib.auth import authenticate, login, logout
# from django.urls import reverse
# from .models import Profile
# from django.http import JsonResponse
# from django.contrib import messages
# from decimal import Decimal
# from django.utils.timezone import now
# import random
# # Home Page
# def homepage(request):
#     return render(request,'home.html')

# def openacc(request):
#     return render(request,'openacc.html') 

# users = User.objects.all()
# # for u in users:
# #     if u.username != "admin":
# #         u.delete()
# # Signup View
# def signup(request):
#     msg = ""
#     if request.method == "POST":
#         email = request.POST.get("email")
#         password = request.POST.get("password")
#         print("------------",password)
#         firstname = request.POST.get("firstname")
#         lastname = request.POST.get("lastname")
#         number = request.POST.get("number")
#         pin = request.POST.get("pin")

#         # Check if user already exists
#         if User.objects.filter(username=email).exists():
#             msg = "User with this email already exists."
#             return render(request, 'home.html', {'msg': msg})

#         # Create User
#         user = User.objects.create(username=email, email=email, password=password)
#         user.set_password(password)
#         user.first_name = firstname
#         user.last_name = lastname
#         user.save()

#         # Create Profile
#         Profile.objects.create(
#             user=user,
#             Firstname=firstname,
#             Lastname=lastname,
#             Email=email,
#             Phonenumber=number,
#             Pin=pin,
#         )

#         # Automatically log in the user
#         login(request, user)
#         return redirect("homepage")

#     return render(request, 'home.html', {'msg': msg})

# # Login View
# def userlogin(request):
#     msg = ""
#     if request.method == "POST":
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(email,password)
#         # Authenticate user
#         user = authenticate(username=email, password=password)
#         print(user)
#         if user is not None:
#             print("----------------")
#             login(request, user)
#             return HttpResponseRedirect(reverse('homepage'))
#         else:
#             msg = "Invalid login credentials"
    

#     return HttpResponseRedirect(reverse('homepage'))

# # Logout View
# def userlogout(request):
#     logout(request)
#     return HttpResponseRedirect(reverse("homepage"))


# #account section

# def account_dashboard(request):
#     account = Account.objects.get(user=request.user)

#     # This month start
#     start_month = now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)

#     # Credits & Debits this month
#     total_credits = Transaction.objects.filter(
#         account=account,
#         transaction_type="credit",
#         timestamp__gte=start_month
#     ).aggregate(total=models.Sum("amount"))["total"] or 0

#     total_debits = Transaction.objects.filter(
#         account=account,
#         transaction_type="debit",
#         timestamp__gte=start_month
#     ).aggregate(total=models.Sum("amount"))["total"] or 0

#     # Recent transactions (last 10)  👉 order_by("-timestamp") aakki latest first
#     transactions = Transaction.objects.filter(account=account).order_by("-timestamp")[:10]

#     return render(request, "account.html", {
#         "account": account,
#         "total_credits": total_credits,
#         "total_debits": total_debits,
#         "transactions": transactions,
#     })


# def transfer(request):
#     if request.method == "POST":
#         recipient_acc_no = request.POST.get("recipient_account")
#         amount = Decimal(request.POST.get("amount"))
#         description = request.POST.get("description", "")

#         sender_account = Account.objects.get(user=request.user)
#         print(sender_account)
#         # 🔹 Check recipient exists
#         try:
#             recipient_account = Account.objects.get(account_number=recipient_acc_no)
#             print("------",recipient_account)
#         except Account.DoesNotExist as e:
#             print(e)
#             messages.error(request, "❌ Recipient account not found.")
#             return redirect("account_dashboard")

#         # 🔹 Save MoneyTransfer (models.py handle cheyyum balance + transactions)
#         try:
#             MoneyTransfer.objects.create(
#                 sender=sender_account,
#                 recipient=recipient_account,
#                 amount=amount,
#                 description=description
#             )
#             Transaction.objects.create(account = sender_account,transaction_type = "debit",amount = amount,description = f"{amount} debited from account")
#             Transaction.objects.create(account = recipient_account,transaction_type = "credit",amount = amount,description = f"{amount} credited to your account")
#             sender_account.balance = sender_account.balance - amount
#             sender_account.save()
#         except ValueError as e:
#             print(e)
#             messages.error(request, f"❌ {str(e)}")
#             return redirect("account_dashboard")

#         messages.success(request, f"✅ ₹{amount} transferred successfully!")
#         return redirect("account_dashboard")
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models import Sum
from .models import *
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import JsonResponse
from django.contrib import messages
from decimal import Decimal
from django.utils.timezone import now


# Home Page
def homepage(request):
    return render(request, 'home.html')


def openacc(request):
    return render(request, 'openacc.html')


# Signup View
def signup(request):
    msg = ""
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        firstname = request.POST.get("firstname")
        lastname = request.POST.get("lastname")
        number = request.POST.get("number")
        pin = request.POST.get("pin")

        # Check if user already exists
        if User.objects.filter(username=email).exists():
            msg = "User with this email already exists."
            return render(request, 'home.html', {'msg': msg})

        # ✅ Create User properly
        user = User(username=email, email=email, first_name=firstname, last_name=lastname)
        user.set_password(password)  # important for login to work
        user.save()

        # ✅ Create Profile
        Profile.objects.create(
            user=user,
            Firstname=firstname,
            Lastname=lastname,
            Email=email,
            Phonenumber=number,
            Pin=pin,
        )

        # ✅ Create Account (auto account_number is generated in model)
        Account.objects.create(user=user, balance=0.00)

        # ✅ Automatically log in the user
        login(request, user)
        return redirect("homepage")

    return render(request, 'home.html', {'msg': msg})


# Login View
def userlogin(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate user
        user = authenticate(username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.error(request, "❌ Invalid login credentials")
            return redirect('homepage')

    return redirect('homepage')


# Logout View
def userlogout(request):
    logout(request)
    return redirect("homepage")


# Account Dashboard
def account_dashboard(request):
    try:
        account = Account.objects.get(user=request.user)
    except Account.DoesNotExist:
        messages.error(request, "❌ No account found. Please create one.")
        return redirect("homepage")

    # This month start
    start_month = now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)

    # Credits & Debits this month
    total_credits = Transaction.objects.filter(
        account=account,
        transaction_type="credit",
        timestamp__gte=start_month
    ).aggregate(total=Sum("amount"))["total"] or 0

    total_debits = Transaction.objects.filter(
        account=account,
        transaction_type="debit",
        timestamp__gte=start_month
    ).aggregate(total=Sum("amount"))["total"] or 0

    # Recent transactions (last 10, newest first)
    transactions = Transaction.objects.filter(account=account).order_by("-timestamp")[:10]

    return render(request, "account.html", {
        "account": account,
        "total_credits": total_credits,
        "total_debits": total_debits,
        "transactions": transactions,
    })


# Money Transfer
def transfer(request):
    if request.method == "POST":
        recipient_acc_no = request.POST.get("recipient_account")
        amount = Decimal(request.POST.get("amount"))
        description = request.POST.get("description", "")

        sender_account = Account.objects.get(user=request.user)

        # 🔹 Check recipient exists
        try:
            recipient_account = Account.objects.get(account_number=recipient_acc_no)
        except Account.DoesNotExist:
            messages.error(request, "❌ Recipient account not found.")
            return redirect("account_dashboard")

        # 🔹 Ensure sender has enough balance
        if sender_account.balance < amount:
            messages.error(request, "❌ Insufficient balance.")
            return redirect("account_dashboard")

        # 🔹 Save MoneyTransfer and Transactions
        try:
            MoneyTransfer.objects.create(
                sender=sender_account,
                recipient=recipient_account,
                amount=amount,
                description=description
            )

            # Transactions
            Transaction.objects.create(
                account=sender_account,
                transaction_type="debit",
                amount=amount,
                description=f"{amount} debited from account"
            )
            Transaction.objects.create(
                account=recipient_account,
                transaction_type="credit",
                amount=amount,
                description=f"{amount} credited to your account"
            )

            # Update balances
            sender_account.balance -= amount
            recipient_account.balance += amount
            sender_account.save()
            recipient_account.save()

        except ValueError as e:
            messages.error(request, f"❌ {str(e)}")
            return redirect("account_dashboard")

        messages.success(request, f"✅ ₹{amount} transferred successfully!")
        return redirect("account_dashboard")