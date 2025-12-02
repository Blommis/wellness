from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Supplement
from .models import MealPlan
from recipes.models import Breakfast, Lunch, Snack
from django.forms import modelform_factory
from django.contrib.admin.views.decorators import staff_member_required

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


def supplement_image(request, pk):
    supplement = get_object_or_404(Supplement, pk=pk)
    return render(request, "products/supplement_image.html",
                  {"supplement": supplement})


"""
Supplement CRUD views for staff dashboard.

Provides full create, read, update, and delete functionality for managing
supplement products within the admin dashboard. Only accessible to staff
users via @staff_member_required decorators.
"""

# Dashboard


@staff_member_required
def products_dashboard(request):
    return render(request, "products/admin/products_dashboard.html")


# List
@staff_member_required
def supplement_list(request):
    items = Supplement.objects.all()
    return render(request, "products/admin/supplement_list.html",
                  {"items": items})


# Add supplement
@staff_member_required
def supplement_create(request):
    SupplementForm = modelform_factory(Supplement, fields="__all__")

    if request.method == "POST":
        form = SupplementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplement created successfully!")
            return redirect("products:supplement_list")
        messages.error(request,
                       "Failed to create supplement. Please fix the errors.")
    else:
        form = SupplementForm()

    return render(request, "products/admin/supplement_form.html",
                  {"form": form})

# Change supplement


@staff_member_required
def supplement_edit(request, pk):
    item = get_object_or_404(Supplement, pk=pk)
    SupplementForm = modelform_factory(Supplement, fields="__all__")

    if request.method == "POST":
        form = SupplementForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Supplement updated successfully!")
            return redirect("products:supplement_list")
        messages.error(request, "Update failed. Please check the errors.")
    else:
        form = SupplementForm(instance=item)

    return render(request, "products/admin/supplement_form.html",
                  {"form": form})


# Delete supplement
@staff_member_required
def supplement_delete(request, pk):
    item = get_object_or_404(Supplement, pk=pk)

    if request.method == "POST":
        item.delete()
        messages.success(request, "Supplement successfully deleted!")
        return redirect("products:supplement_list")

    return render(request, "products/admin/supplement_delete.html",
                  {"item": item})


# MEALPLAN CRUD
@staff_member_required
def mealplan_list(request):
    items = MealPlan.objects.all()
    return render(request, "products/admin/mealplan_list.html",
                  {"items": items})


@staff_member_required
def mealplan_create(request):
    MealPlanForm = modelform_factory(MealPlan, fields="__all__")

    if request.method == "POST":
        form = MealPlanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Mealplan created successfully!")
            return redirect("products:mealplan_list")
        messages.error(request,
                       "Failed to create mealplan. Please correct the errors.")
    else:
        form = MealPlanForm()

    return render(request, "products/admin/mealplan_form.html", {"form": form})


@staff_member_required
def mealplan_edit(request, pk):
    item = get_object_or_404(MealPlan, pk=pk)
    MealPlanForm = modelform_factory(MealPlan, fields="__all__")

    if request.method == "POST":
        form = MealPlanForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Mealplan updated successfully!")
            return redirect("products:mealplan_list")
        messages.error(request, "Update failed. Please fix the errors.")
    else:
        form = MealPlanForm(instance=item)

    return render(request, "products/admin/mealplan_form.html", {"form": form})


@staff_member_required
def mealplan_delete(request, pk):
    item = get_object_or_404(MealPlan, pk=pk)

    if request.method == "POST":
        item.delete()
        messages.success(request, "Mealplan deleted successfully!")
        return redirect("products:mealplan_list")

    return render(request, "products/admin/mealplan_delete.html",
                  {"item": item})
