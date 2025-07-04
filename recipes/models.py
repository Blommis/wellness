from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class RecipeBase(models.Model):
    """Abstract base model for shared fields"""
    name = models.CharField(max_length=100)
    short_description = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    image = CloudinaryField('image', blank=True, null=True)

    class Meta: 
        abstract = True
    
    def __str__(self):
        return self.name


class Breakfast(RecipeBase):
    class Meta:
        verbose_name_plural = "Breakfast Recipes"


class Lunch (RecipeBase):
    class Meta:
        verbose_name_plural = "Lunch Recipes"


class Snack(RecipeBase):
    class Meta:
        verbose_name_plural = "Snack Recipes"





