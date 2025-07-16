from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Supplement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=50, unique=True)
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.name


class MealPlan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    calories = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def __str__(self):
        return self.name
