from django.db import models

# Create your models here.

class Supplement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=50, unique=True)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name