# serializers.py
from rest_framework import serializers
from .models import Product, Images

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = '__all__'

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('id', 'image')

class ProductSerializer(serializers.ModelSerializer):
    image_set = ImagesSerializer(many=True, read_only=True)  # Update the field name

    class Meta:
        model = Product
        fields = ('id', 'name', 'typeid', 'price', 'discount', 'pic', 'count', 'material', 'brand', 'description', 'image_set')
