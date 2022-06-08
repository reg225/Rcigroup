from asyncio.windows_events import NULL
from email.mime import image
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    
        
    def __str__(self):
        return self.name
class offer(models.Model):
    stock = models.IntegerField()
    discription = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
