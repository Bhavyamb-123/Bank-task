"""
URL configuration for Bankproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from BankApp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage,name="homepage"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.userlogin,name="login"),
    path('logout/',views.userlogout,name="logout"),
    path("open-account/", views.open_account, name="open-account"),
    path('openacc/',views.openacc,name="openacc"),
    path('account_dashboard/',views.account_dashboard,name="account_dashboard"),
    path('transfer/',views.transfer,name="transfer"),
     # Credit Card
    path("creditcard/", views.credit_card_page, name="creditcard"),
    path("apply-creditcard/", views.apply_creditcard, name="apply_creditcard"),

    # Debit Card
    path("debitcard/", views.debit_card_page, name="debitcard"),
    path("apply-debitcard/", views.apply_debitcard, name="apply_debitcard"),
]
