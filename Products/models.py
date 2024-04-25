from django.db import models
from django.urls import reverse

from Accounts.models import Account
from Category.models import SubCategory

class Product(models.Model):
    Product_name = models.CharField(max_length=200, unique=True)
    Slug = models.CharField(max_length=200, unique=True)
    Description = models.CharField(max_length=500, blank=True)
    Images = models.CharField( max_length=250)
    Is_available = models.BooleanField(default=True)
    SubCategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True)
    Created_date = models.DateTimeField( auto_now_add=True)
    Modified_date = models.DateTimeField( auto_now=True)

    
    def get_url(self):
        return reverse('product_detail', args=[self.Category.Slug, self.Slug])

    def __str__(self):
        return self.Product_name


class Quotes(models.Model):
    user = models.ForeignKey(Account,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)