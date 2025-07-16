from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Supplement
from .models import MealPlan
from recipes.models import Breakfast, Lunch, Snack

# Create your views here.


def search_results(request):
    """ Handles search queries for supplements, meal plans, and recipes. """
    query = request.GET.get('q')
    supplements = []
    mealplans = []
    breakfast_recipes = []
    lunch_recipes = []
    snack_recipes = []

    if query in ['supplement', 'supplements']:
        return redirect('products:supplements')

    if query in ['mealplan', 'mealplans']:
        return redirect('products:view_mealplan')

    if query in ['recipe', 'recipes']:
        return redirect('recipes:recipes')

    if query:
        supplements = Supplement.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        mealplans = MealPlan.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

        breakfast_recipes = Breakfast.objects.filter(
            Q(name__icontains=query)
            | Q(short_description__icontains=query)
            | Q(description__icontains=query)
        )
        lunch_recipes = Lunch.objects.filter(
            Q(name__icontains=query)
            | Q(short_description__icontains=query)
            | Q(description__icontains=query)
        )
        snack_recipes = Snack.objects.filter(
            Q(name__icontains=query)
            | Q(short_description__icontains=query)
            | Q(description__icontains=query)
        )
    else:
        messages.error(request, "Please enter a search term.")
        return redirect('home')
    context = {
        'query': query,
        'supplements': supplements,
        'mealplans': mealplans,
        'breakfast_recipes': breakfast_recipes,
        'lunch_recipes': lunch_recipes,
        'snack_recipes': snack_recipes,
    }
    return render(request, 'products/search_results.html', context)


def supplements(request):
    """A view to show the supplement page"""

    supplements = Supplement.objects.all()

    context = {
        'supplements': supplements,
    }
    return render(request, 'products/supplements.html', context)


def supplement_detail(request, pk):
    """ A view showing more detail for each supplement """
    supplement = get_object_or_404(Supplement, pk=pk)

    context = {
        'supplement': supplement,
    }
    return render(request, 'products/supplement_detail.html', context)


def view_mealplan(request):
    """ A view that shows mealplans content """
    mealplans = MealPlan.objects.all()

    context = {
        'mealplans': mealplans,
    }

    return render(request, 'products/mealplan.html', context)
