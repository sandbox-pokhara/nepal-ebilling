from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class PaymentMode(models.TextChoices):
    CASH = "Cash"
    CREDIT_CARD = "Credit Card"
    CHEQUE = "Cheque"


FISCAL_YEAR_CHOICES = [("2081-82", "2081-82")]


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField()
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.username


class Sales(models.Model):
    fiscal_year = models.CharField(
        max_length=7,
        choices=FISCAL_YEAR_CHOICES,
        default="2081-82",
    )
    party_name = models.CharField(max_length=255)
    payment_mode = models.CharField(
        max_length=11,
        choices=PaymentMode,
        default="Cash",
    )
    party_pan = models.CharField(max_length=9)
    address = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    particulars = models.CharField(max_length=255)
    quantity = models.PositiveSmallIntegerField(default=1)
    date = models.DateField(auto_now_add=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Sale {self.id}"


class Invoice(models.Model):
    sales = models.ForeignKey(Sales, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice {self.id} for {self.customer}"
