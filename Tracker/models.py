# from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class URLS(models.Model):
    url = models.URLField(null = False)

class Product(models.Model):
    name = models.CharField(max_length=500)
    url = models.OneToOneField(URLS, on_delete=models.CASCADE)
    price_history = models.TextField()

class Price_History(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()

# class UserCart(models.Model):
#     name = models.CharField(max_length=100)
#     url = models.URLField() 

class wishlist(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)