# from django.db import models
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=500)
    url = models.URLField(unique=True)
    image_url = models.URLField(default='https://bitsofco.de/content/images/2018/12/Screenshot-2018-12-16-at-21.06.29.png')
    rating = models.FloatField(default=0)
    price_history = models.ManyToManyField("PriceHistory", related_name='PriceHistoryProduct')

class PriceHistory(models.Model):
    product = models.ForeignKey(Product, null=True, related_name='PriceHistoryProduct', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    price = models.FloatField()
    
    class Meta:
        get_latest_by = 'date'

class wishlist(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE)