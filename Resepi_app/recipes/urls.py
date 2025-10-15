from django.urls import path
from .views import (
    RecipeListCreateView, 
    CategoryListCreateView, 
    IngerdientListCreateView, 
    RecipeDetailview
)

urlpatterns = [
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailview.as_view(), name='recipe-detail'),
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('ingredients/', IngerdientListCreateView.as_view(), name='ingredient-list'),
]
