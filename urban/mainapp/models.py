from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
      name=models.CharField(max_length=50)
      stock=models.IntegerField()
      description=models.CharField(max_length=100)
      price=models.IntegerField()
      accessories=models.CharField(max_length=50)
      bookingamount=models.IntegerField()
      image=models.ImageField()
      seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products_sold')


 
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)     

