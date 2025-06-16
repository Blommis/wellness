from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Supplement
# Create your views here.


def supplements(request):
    """A view to show the supplement page"""

    supplements = Supplement.objects.all()
    query = None

    if request.GET: 
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Coulndt find your wishing product")
                return redirect(reverse('supplements'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            supplements = supplements.filter(queries)

    context = {
        'supplements': supplements,
        'search_term': query,
    }
    return render(request, 'products/supplements.html', context)

def supplement_detail(request, pk):
    supplement = get_object_or_404(Supplement, pk=pk)

    context = {
        'supplement': supplement,
    }
    return render(request, 'products/supplement_detail.html', context)