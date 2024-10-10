from django.db import models

# Create your models here.
class product(models.Model):
      name=models.CharField(max_length=50)
      stock=models.IntegerField()
      description=models.CharField(max_length=100)
      price=models.IntegerField()
      accessories=models.CharField(max_length=50)
      bookingamount=models.IntegerField()
      image=models.ImageField()

      
      