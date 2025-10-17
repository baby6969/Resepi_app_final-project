from django.urls import path
from .views import (
    RecipeListCreateView, 
    CategoryListCreateView, 
    IngerdientListCreateView, 
    RecipeDetailview,
    RecipeSearchView
)

urlpatterns = [
    path('', RecipeListCreateView.as_view(), name='recipe-list'),
    path('<int:pk>/', RecipeDetailview.as_view(), name='recipe-detail'),
    path('categories/<int:pk>', CategoryListCreateView.as_view(), name='category-list'),
    path('ingredients/', IngerdientListCreateView.as_view(), name='ingredient-list'),
     path("search/", RecipeSearchView.as_view(), name="recipe-search"),
]
