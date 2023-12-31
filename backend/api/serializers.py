# serializers.py
from rest_framework import serializers
from .models import Product, Images, Color, Size, Sliders, Banner


class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Images
        fields = ("id", "image")


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ("id", "color")


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ("id", "size")


class ProductSerializer(serializers.ModelSerializer):
    images = ImagesSerializer(many=True, read_only=True, source="images_set")
    colors = ColorSerializer(many=True, read_only=True, source="colors_set")
    size = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "discount",
            "pic",
            "count",
            "material",
            "brand",
            "description",
            "images",
            "colors",
            "size",
            "category",
        )

    def get_size(self, instance):
        return instance.size.values_list("size", flat=True)

    def get_category(self, instance):
        return instance.category.values_list("category", flat=True)


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sliders
        fields = "__all__"


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
