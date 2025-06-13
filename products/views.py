from django.shortcuts import render
from .models import Supplement
# Create your views here.


def supplements(request):
    """A view to show the supplement page"""

    supplements = Supplement.objects.all()

    context = {
        'supplements': supplements, 
    }
    return render(request, 'products/supplements.html', context)