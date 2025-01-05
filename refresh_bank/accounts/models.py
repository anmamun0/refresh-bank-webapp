from django.db import models
from django.contrib.auth.models import User 
from bank_info.models import Bank
# Create your models here.
from django.core.exceptions import ObjectDoesNotExist
from .constants import ACCOUNT_TYPE,GENDER_TYPE

def get_default_bank():
    try:
        return Bank.objects.first()  # Fetch the first Bank object
    except ObjectDoesNotExist:
        return None  # Return None if no Bank exists

class UserBankAccount(models.Model):
    user = models.OneToOneField(User,related_name='account',on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10,choices=ACCOUNT_TYPE)
    account_no = models.IntegerField(unique=True)
    phone = models.CharField(max_length=14,null=True,blank=True) 
    birth_date = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=10,choices=GENDER_TYPE)
    initial_deposite_date = models.DateField(auto_now_add=True)
    balance = models.DecimalField(default=0,max_digits=12,decimal_places=2)
    bank = models.ForeignKey(Bank, default=get_default_bank , on_delete=models.CASCADE,null=True,blank=True)
    # is_bankrupt = models.BooleanField(default=False) 


    def __str__(self):
        return str(self.account_no)

class UserAddress(models.Model):
    user = models.OneToOneField(User,related_name='address',on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.email}"
