from rest_framework import serializers
from .models import Product, Order, Menu


class ProductSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class MenuSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'