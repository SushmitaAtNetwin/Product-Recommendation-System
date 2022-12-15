from django.db import models

# Create your models here.
# models.py
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='images/')