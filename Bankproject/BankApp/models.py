from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
# from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    Firstname = models.CharField(max_length=25, blank=True, null=True)
    Lastname = models.CharField(max_length=25, blank=True, null=True)
    Email = models.CharField(max_length=500, blank=True, null=True)
    Phonenumber = models.BigIntegerField(default=0, blank=True, null=True)
    Pin = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} Profile"


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    account_number = models.CharField(max_length=20, unique=True, editable=False)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.account_number:
            last_account = Account.objects.all().order_by("id").last()
            if last_account:
                last_number = int(last_account.account_number)
                self.account_number = str(last_number + 1).zfill(12)  # Auto 12-digit
            else:
                self.account_number = "100000000000"  # First account
        super().save(*args, **kwargs)

    def __str__(self):
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

    def __str__(self):
        return f"{self.account.user.username} - {self.transaction_type} ₹{self.amount}"


class MoneyTransfer(models.Model):
    sender = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="sent_transfers")
    recipient = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="received_transfers")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=255, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"₹{self.amount} from {self.sender.account_number} to {self.recipient.account_number}"
    



class CreditCardApplication(models.Model):
    CARD_CHOICES = [
        ('platinum', 'Platinum Card'),
        ('rewards', 'Rewards Card'),
        ('cashback', 'Cashback Card'),
        ('global', 'Global Card'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    income = models.DecimalField(max_digits=12, decimal_places=2)
    cardType = models.CharField(max_length=20, choices=CARD_CHOICES)
    status = models.CharField(max_length=20, default="Pending")  # Pending, Approved, Rejected
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname} - {self.cardType} ({self.status})"


class DebitCardApplication(models.Model):
    CARD_CHOICES = [
        ('classic', 'Classic Debit Card'),
        ('gold', 'Gold Debit Card'),
        ('platinum', 'Platinum Debit Card'),
        ('international', 'International Debit Card'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    fullname = models.CharField(max_length=150)
    email = models.EmailField()
    account_number = models.CharField(max_length=30, null=True, blank=True)
    cardType = models.CharField(max_length=20, choices=CARD_CHOICES)
    status = models.CharField(max_length=20, default="Pending")
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fullname} - {self.cardType} ({self.status})"