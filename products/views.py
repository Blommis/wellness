from django.shortcuts import render, get_object_or_404
from .models import Supplement
# Create your views here.


def supplements(request):
    """A view to show the supplement page"""

    supplements = Supplement.objects.all()

    context = {
        'supplements': supplements, 
    }
    return render(request, 'products/supplements.html', context)

def supplement_detail(request, pk):
    supplement = get_object_or_404(Supplement, pk=pk)

    context = {
        'supplement': supplement,
    }
    return render(request, 'products/supplement_detail.html', context)