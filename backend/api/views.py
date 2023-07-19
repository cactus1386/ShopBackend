from rest_framework import generics
from .models import Product, Sliders, Banner
from .serializers import ProductSerializer, SliderSerializer, BannerSerializer


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SliderListAPIView(generics.ListAPIView):
    queryset = Sliders.objects.all()
    serializer_class = SliderSerializer


class BannerListAPIView(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
