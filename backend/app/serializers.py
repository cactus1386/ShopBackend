# serializers.py
from rest_framework import serializers
from .models import Product, Images, color, size

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ('id', 'image')


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = color
        fields = ('id', 'color')


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = size
        fields = ('id', 'size')



class ProductSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True, source='images_set')
    colors = ColorSerializer(many=True, read_only=True, source='colors_set')
    sizes = SizeSerializer(many=True, read_only=True, source='size_set')

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'discount', 'pic', 'count', 'material', 'brand', 'description', 'images', 'colors', 'sizes')

        
