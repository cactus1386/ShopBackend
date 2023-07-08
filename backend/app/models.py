from django.db import models

# Create your models here.
class Tshirt(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=25)
    discount = models.CharField(max_length=10)
    second_price = models.CharField(max_length=10)
    pic = models.CharField(max_length=255)
    count = models.IntegerField(default=10)


class Pant(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=25)
    discount = models.CharField(max_length=10)
    second_price = models.CharField(max_length=10)
    pic = models.CharField(max_length=255)
    count = models.IntegerField(default=10)


class sock(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=25)
    discount = models.CharField(max_length=10)
    second_price = models.CharField(max_length=10)
    pic = models.CharField(max_length=255)
    count = models.IntegerField(default=10)
    