from django.shortcuts import render, get_object_or_404
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


def recipe_detail(request, category, pk):
    model_map = {
        'breakfast': Breakfast,
        'lunch': Lunch,
        'snack': Snack,
    }
    model = model_map.get(category)
    
    recipe = get_object_or_404(model, pk=pk)

    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'category': category.capitalize(),
    })