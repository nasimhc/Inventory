from email.policy import default
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    shade = models.CharField(max_length=100)
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.CharField(max_length=100)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE,null=True, blank=True)
    product_image = models.ImageField(default='https://m.media-amazon.com/images/I/71wqzv-M41L._SL1500_.jpg')
    
    def __str__(self):
        return self.name