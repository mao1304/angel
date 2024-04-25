from django.db import models

from Accounts.models import Account
from Products. models import Product

class Quotes(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
