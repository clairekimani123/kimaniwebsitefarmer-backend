
from rest_framework import serializers
from .models import Animal, Cart, Order
from djoser.serializers import UserCreateSerializer as DjoserUserCreateSerializer

class UserCreateSerializer(DjoserUserCreateSerializer):
    class Meta(DjoserUserCreateSerializer.Meta):
        fields = ['id', 'email', 'username', 'password', 'is_farmer']

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = ['id', 'name', 'breed', 'category', 'age', 'price', 'image', 'farmer', 'location', 'rating']

class CartSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)
    animal_id = serializers.PrimaryKeyRelatedField(
        queryset=Animal.objects.all(), source='animal', write_only=True
    )

    class Meta:
        model = Cart
        fields = ['id', 'user', 'animal', 'animal_id', 'quantity', 'created_at']

class OrderSerializer(serializers.ModelSerializer):
    animal = AnimalSerializer(read_only=True)
    user = serializers.StringRelatedField(allow_null=True)  # Handle nullable user

    class Meta:
        model = Order
        fields = ['id', 'user', 'animal', 'status', 'created_at']
