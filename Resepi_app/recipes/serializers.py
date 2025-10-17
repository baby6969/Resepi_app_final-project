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
    categories = CategorySerializer(many=True,required=False)
    ingredients = IngredientSerializer(many=True, required =False)

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

    def create(self, validated_data):
        categories_data = validated_data.pop('categories', [])
        ingredients_data = validated_data.pop('ingredients', [])
        recipe = Recipe.objects.create(**validated_data)

    
        for cat in categories_data or []:
            name = (cat or {}).get('name')
            if not name:
                continue
            category, _ = Category.objects.get_or_create(name=name)
            recipe.categories.add(category)

       
        for ing in ingredients_data or []:
            name = (ing or {}).get('name')
            if not name:
                continue
            ingredient, _ = Ingredient.objects.get_or_create(name=name)
            recipe.ingredients.add(ingredient)

        return recipe

    def update(self, instance, validated_data):
        categories_data = validated_data.pop('categories', None)
        ingredients_data = validated_data.pop('ingredients', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

      
        if categories_data is not None:
            instance.categories.clear()
            for cat in categories_data or []:
                name = (cat or {}).get('name')
                if not name:
                    continue
                category, _ = Category.objects.get_or_create(name=name)
                instance.categories.add(category)

        
        if ingredients_data is not None:
            instance.ingredients.clear()
            for ing in ingredients_data or []:
                name = (ing or {}).get('name')
                if not name:
                    continue
                ingredient, _ = Ingredient.objects.get_or_create(name=name)
                instance.ingredients.add(ingredient)

        return instance