from django.shortcuts import render
from .models import Breakfast, Lunch, Snack
# Create your views here.


def recipes(request):
    breakfasts = Breakfast.objects.all()
    lunches = Lunch.objects.all()
    snacks = Snack.objects.all()

    context = {
        'breakfasts': breakfasts,
        'lunches': lunches,
        'snacks': snacks,
    }
    return render(request, 'recipes/recipes.html', context)