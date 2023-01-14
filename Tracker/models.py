# from django.db import models
from djongo import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=500)
    url = models.URLField(null = False)
    price_history = models.TextField()
    notify_user = models.BooleanField(default=1)
    # User = 

class Price_History(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()