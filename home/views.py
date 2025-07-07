from django.shortcuts import render
from .models import Event
from datetime import date
# Create your views here.


def index(request):
    """View to return the index page with upcoming events"""
    events = Event.objects.filter(date__gte=date.today()).order_by('date')
    return render(request, 'home/index.html', {'events': events})

