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
    
class Account(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    account_number = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)

    def _str_(self):
        return f"{self.user.username} - {self.account_number}"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ("credit", "Credit"),
        ("debit", "Debit"),
    ]

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="transactions")
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.account.user.username} - {self.transaction_type} ₹{self.amount}"
    
class MoneyTransfer(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="sent_transfers")
    recipient = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="received_transfers")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"Transfer ₹{self.amount} from {self.sender.account_number} to {self.recipient.account_number}"
