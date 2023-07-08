from rest_framework import serializers
from .models import Tshirt, Pant, sock

class TshirtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tshirt
        fields = '__all__'

class PantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pant
        fields = '__all__'
