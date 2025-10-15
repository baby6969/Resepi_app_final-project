from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Recipe, Category, Ingredient


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'name']


class RecipeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    categories = CategorySerializer(many=True, read_only=True)
    ingredients = IngredientSerializer(many=True, read_only=True)

    class Meta:
        model = Recipe
        fields = [
            'id',
            'user',
            'title',
            'description',
            'instructions',
            'categories',
            'ingredients',
            'created_at',
        ]
