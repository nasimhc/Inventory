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
    
    def __str__(self):
        return self.name