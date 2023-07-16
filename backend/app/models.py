# models.py
from django.db import models
import datetime

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField(max_length=25)
    discount = models.IntegerField(max_length=10)
    pic = models.CharField(max_length=255, null=True, blank=True)
    count = models.IntegerField(default=10)
    material = models.CharField(max_length=255)
    brand = models.CharField(max_length=500)
    description = models.TextField(max_length=100000)
    created_date = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.name

    def snnipets(self):
        return self.description[:100] + "..."

class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images_set')
    image = models.CharField(max_length=255, blank=True, null=True, default="")

    def __str__(self):
        return self.image


class color(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="colors_set")
    color = models.CharField(max_length=255, blank=True, null=True, default="")

    def __str__(self):
        return self.color
    

class size(models.Model):
    CHOICES = (
        ("S", "S"),
        ("M", "M"),
        ("L", 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('3XL', "3XL")
        )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="size_set")
    size = models.CharField(max_length=255, blank=True, null=True, default="", choices=CHOICES)

    def __str__(self):
        return self.size


class Sliders(models.Model):
    link = models.CharField(max_length=10000)
    image = models.CharField(max_length=10000)

    def __str__(self):
        return self.image
    
class banner(models.Model):
    link = models.CharField(max_length=10000)
    image = models.CharField(max_length=10000)

    def __str__(self):
        return f"banner {self.id}"
