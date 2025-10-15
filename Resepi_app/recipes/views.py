from unicodedata import category
from warnings import catch_warnings
from django.shortcuts import render
from rest_framework import generics , permissions
from .models import Recipe ,Category , Ingredient
from .serializers import RecipeSerializer, CategorySerializer, IngredientSerializer



class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_created (self, serializer):
                serializer.save(user=self.request.user)
                
class RecipeDetailview(generics.RetrieveUpdateDestroyAPIView):
        queryset =Recipe.objects.all()
        serializer_class = RecipeSerializer
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class CategoryListCreateView(generics.ListCreateAPIView):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        
class IngerdientListCreateView(generics.ListCreateAPIView):
        queryset = Ingredient.objects.all()
        serializer_class = IngredientSerializer
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]
