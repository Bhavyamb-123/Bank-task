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
        ('checking', 'Checking'),
        ('savings', 'Savings'),
    ]

    EMPLOYMENT_STATUS = [
        ('employed', 'Employed'),
        ('self-employed', 'Self-Employed'),
        ('unemployed', 'Unemployed'),
        ('retired', 'Retired'),
        ('student', 'Student'),
    ]

    INCOME_RANGES = [
        ('under-25k', 'Under $25,000'),
        ('25k-50k', '$25,000 - $50,000'),
        ('50k-75k', '$50,000 - $75,000'),
        ('75k-100k', '$75,000 - $100,000'),
        ('over-100k', 'Over $100,000'),
    ]
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES,blank=True,null=True)
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=15,blank=True,null=True)
    date_of_birth = models.DateField(blank=True,null=True)
    ssn = models.CharField(max_length=11,blank=True,null=True)  # format XXX-XX-XXXX
    address = models.CharField(max_length=255,blank=True,null=True)
    city = models.CharField(max_length=100,blank=True,null=True)
    state = models.CharField(max_length=50,blank=True,null=True)
    zip_code = models.CharField(max_length=10,blank=True,null=True)
    employment = models.CharField(max_length=20, choices=EMPLOYMENT_STATUS,blank=True,null=True)
    income = models.CharField(max_length=20, choices=INCOME_RANGES,blank=True,null=True)
    document_upload = models.FileField(upload_to="documents/", null=True, blank=True)

    # Security Questions
    pet_name = models.CharField(max_length=100,blank=True,null=True)
    birth_city = models.CharField(max_length=100, null=True, blank=True)


    # Deposit
    initial_deposit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # Terms & Marketing
    terms_accepted = models.BooleanField(default=False)
    marketing_opt_in = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.account_type}"
