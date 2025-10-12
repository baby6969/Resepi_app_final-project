from django.db import models
from django.contrib.auth.models import User


class Category (models.Model):
    name = models.CharField (max_length = 100)
  
    
    def __str__(self):
     return self.name


class Ingredient(models.Model):
  name = models.CharField (max_length= 100)
  
  def __str__(self):
    return self.name

class Recipe (models.Model):
    user  = models.ForeignKey(User, on_delete=models.CASCADE,related_name="recipes")
    title =models.CharField (max_length =200)
    description = models.TextField()
    instructions =models.TextField()
    categories =models.ManyToManyField(Category, related_name="recipes")
    ingredients =models.ManyToManyField(Ingredient, related_name="recipes")
    created_at = models.DateTimeField(auto_now_add=True)