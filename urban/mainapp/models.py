from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):
      name=models.CharField(max_length=50)
      stock=models.IntegerField()
      description=models.CharField(max_length=100)
      price=models.IntegerField()
      accessories=models.CharField(max_length=50)
      bookingamount=models.IntegerField()
      image=models.ImageField()

 
class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)     

