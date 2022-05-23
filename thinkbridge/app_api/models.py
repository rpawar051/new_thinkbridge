from django.db import models

# Create your models here.

class CartItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.FloatField()
    basic_fields = models.CharField(max_length=200)
    product_quantity = models.PositiveIntegerField()