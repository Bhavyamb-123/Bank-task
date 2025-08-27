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
        return f"{self.user.first_name} {self.user.last_name} Profile"

class AccountApplication(models.Model):
    ACCOUNT_TYPES = [
        ('checking', 'Checking Account'),
        ('savings', 'Savings Account'),
    ]

    EMPLOYMENT_STATUS = [
        ('employed', 'Employed'),
        ('self-employed', 'Self-Employed'),
        ('unemployed', 'Unemployed'),
        ('retired', 'Retired'),
        ('student', 'Student'),
    ]

    INCOME_RANGE = [
        ('under-25k', 'Under ₹25,000'),
        ('25k-50k', '₹25,000 - ₹50,000'),
        ('50k-75k', '₹50,000 - ₹75,000'),
        ('75k-100k', '₹75,000 - ₹100,000'),
        ('over-100k', 'Over ₹100,000'),
    ]

    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="applications")
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)
    date_of_birth = models.DateField()
    ssn = models.CharField(max_length=20)  # You might later want to encrypt this
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    employment_status = models.CharField(max_length=20, choices=EMPLOYMENT_STATUS)
    annual_income = models.CharField(max_length=20, choices=INCOME_RANGE)

    # Identity Verification
    id_document = models.FileField(upload_to="id_documents/", null=True, blank=True)
    security_question1 = models.CharField(max_length=255)
    security_question2 = models.CharField(max_length=255)

    # Review
    initial_deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    agree_terms = models.BooleanField(default=False)
    agree_marketing = models.BooleanField(default=False)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Application of {self.profile.Firstname} {self.profile.Lastname} - {self.account_type}"

