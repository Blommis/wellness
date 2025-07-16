from django.shortcuts import render
from .models import GalleryImage
# Create your views here.


def about(request):
    images = GalleryImage.objects.all()
    return render(request, 'about/about.html', {'images': images})
