# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    typeid = models.IntegerField(default=1)
    price = models.IntegerField(max_length=25)
    discount = models.IntegerField(max_length=10)
    pic = models.CharField(max_length=255, null=True, blank=True)
    count = models.IntegerField(default=10)
    material = models.CharField(max_length=255)
    brand = models.CharField(max_length=500)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.name


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.CharField(max_length=255, blank=True, null=True, default="")

    def __str__(self):
        return self.image

# class color(models.Model):
#     pid = models.IntegerField()
#     color = models.CharField(max_length=255)


# class sizenum(models.Model):
#     pid = models.IntegerField()
#     sizenum = models.IntegerField()


# class sizetype(models.Model):
#     pid = models.IntegerField()
#     sizetype = models.CharField(max_length=10)
    
    