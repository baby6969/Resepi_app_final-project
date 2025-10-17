from rest_framework import generics, permissions,filters
from .models import Recipe, Category, Ingredient
from .serializers import RecipeSerializer, CategorySerializer, IngredientSerializer
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100


class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ["created_at", "title"]

 
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RecipeDetailview(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    # only permission user can add ,delete and update 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class IngerdientListCreateView(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


# Search endpoint ingredient and category and q (free text)
class RecipeSearchView(generics.ListAPIView):
    serializer_class = RecipeSerializer
    permission_classes = [permissions.AllowAny]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        qs = Recipe.objects.all().distinct()
        ingredient = self.request.query_params.get("ingredient")
        category = self.request.query_params.get("category")
        q = self.request.query_params.get("q")

        if ingredient:
            qs = qs.filter(ingredients__name__icontains=ingredient)
        if category:
            qs = qs.filter(categories__name__icontains=category)
        if q:
            qs = qs.filter(
                Q(title__icontains=q) |
                Q(description__icontains=q) |
                Q(instructions__icontains=q) |
                Q(ingredients__name__icontains=q) |
                Q(categories__name__icontains=q)
            )
        return qs.order_by("-created_at")