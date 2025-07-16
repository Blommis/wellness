from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    image = CloudinaryField('image', blank=True, null=True)

    def __str__(self):
        return self.title
