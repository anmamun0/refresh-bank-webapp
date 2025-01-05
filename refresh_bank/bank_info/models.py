from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

STATUS_CHOICE = [
    ('Active', 'Active'), 
    ('Inactive', 'Inactive'), 
    ('Maintenance', 'Maintenance')
]
# Create your models here.

class Bank(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True, null=True, blank=True)  # Unique identifier like SWIFT code
    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=20, null=True, blank=True)  # Contact number
    email = models.EmailField(null=True, blank=True)  # Email address
    total_money = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    opening_date = models.DateField(auto_now_add=True,null=True,blank=True)  # Opening date of the bank
    status = models.CharField(max_length=30, choices=STATUS_CHOICE, default='Active')  # Status of the bank
    
      
    def save(self, *args, **kwargs): 
        if Bank.objects.exists() and not self.pk:
            raise ValidationError("Only one instance of Bank is allowed.")
        super().save(*args, **kwargs)