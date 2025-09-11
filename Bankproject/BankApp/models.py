from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Profile(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    Firstname=models.CharField(max_length=25,blank=True,null=True)
    Lastname=models.CharField(max_length=25,blank=True,null=True)
    Email=models.CharField(max_length=500,blank=True,null=True)
    Phonenumber=models.IntegerField(default=0,blank=True,null=True)
    Pin=models.IntegerField(default=0,blank=True,null=True)
    def __str__(self):
        return self.user.firstname + "profile"
    
    from django.db import models

class LoanApplication(models.Model):
    # Loan Details
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    loan_purpose = models.CharField(max_length=50)
    property_type = models.CharField(max_length=50)
    down_payment = models.DecimalField(max_digits=12, decimal_places=2)

    # Personal Information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    marital_status = models.CharField(max_length=20)
    current_address = models.TextField()

    # Financial Information
    employment_type = models.CharField(max_length=50)
    monthly_income = models.DecimalField(max_digits=12, decimal_places=2)
    work_experience = models.IntegerField()
    company_name = models.CharField(max_length=150)
    existing_loans = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    credit_score = models.IntegerField(blank=True, null=True)

    # Property Details
    property_value = models.DecimalField(max_digits=12, decimal_places=2)
    property_age = models.CharField(max_length=50)
    property_city = models.CharField(max_length=100)
    property_area = models.IntegerField()
    property_address = models.TextField()

    # Submission Info
    agree_terms = models.BooleanField(default=False)
    credit_check = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Loan Application - {self.first_name} {self.last_name} ({self.loan_amount})"

