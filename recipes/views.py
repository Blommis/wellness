from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Breakfast, Lunch, Snack
from django.db import models
from reviews.forms import ReviewForm
from reviews.models import Review
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from django.contrib import messages

# Create your views here.


def recipes(request):
    """
    Renders the recipes page with all breakfasts, lunches, and snacks,
    each annotated with their number of associated reviews.
    """
    breakfasts = annotate_with_review_count(Breakfast.objects.all(), Breakfast)
    lunches = annotate_with_review_count(Lunch.objects.all(), Lunch)
    snacks = annotate_with_review_count(Snack.objects.all(), Snack)

    context = {
        'breakfasts': breakfasts,
        'lunches': lunches,
        'snacks': snacks,
    }
    return render(request, 'recipes/recipes.html', context)


def annotate_with_review_count(queryset, model):
    """
    Adds a 'review_count' attribute to each object to indicate how many reviews
    it has. Useful for displaying review info in recipe listings.
    """
    content_type = ContentType.objects.get_for_model(model)
    for item in queryset:
        item.review_count = Review.objects.filter(
            content_type=content_type, object_id=item.pk
        ).count()
    return queryset


def recipe_detail(request, category, pk):
    """
    Handles the display of a specific recipe's details and reviews.
    If the user is authenticated and submits a valid review form,
    the review is saved and the page is reloaded.
    """
    model_map = {
        'breakfast': Breakfast,
        'lunch': Lunch,
        'snack': Snack,
    }
    model = model_map.get(category)

    recipe = get_object_or_404(model, pk=pk)

    content_type = ContentType.objects.get_for_model(model)
    reviews = Review.objects.filter(content_type=content_type, object_id=pk)

    average_rating = reviews.aggregate(models.Avg('rating'))['rating__avg']

    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.content_type = content_type
            review.object_id = pk
            review.save()
            return redirect('recipes:recipe_detail', category=category, pk=pk)
    else:
        form = ReviewForm()

    return render(request, 'recipes/recipe_detail.html', {
        'recipe': recipe,
        'category': category.capitalize(),
        'reviews': reviews,
        'average_rating': average_rating,
        'form': form,
    })


@login_required
def delete_review(request, review_id):
    """ user as authenticated can delete their own reviews"""

    review = get_object_or_404(Review, id=review_id)
    if review.user != review.user:
        return redirect('recipes:recipes')

    category = review.content_type.model
    object_id = review.object_id

    review.delete()

    return redirect('recipes:recipe_detail', category=category, pk=object_id)


# Admin dashboard (choose category)
@staff_member_required
def recipe_dashboard(request):
    return render(request, "recipes/admin/dashboard.html")


# List recipes
@staff_member_required
def recipe_list(request, category):
    model = {"breakfast": Breakfast, "lunch": Lunch,
             "snack": Snack}.get(category)
    items = model.objects.all()
    return render(
        request, "recipes/admin/recipe_list.html",
        {"items": items, "category": category})


# Create recipe
@staff_member_required
def recipe_create(request, category):
    model = {"breakfast": Breakfast, "lunch": Lunch,
             "snack": Snack}.get(category)

    DynamicRecipeForm = modelform_factory(model, fields="__all__")

    if request.method == "POST":
        form = DynamicRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"{category.title()} recipe created successfully!")
            return redirect("recipes:recipe_list", category=category)
        messages.error(
            request, "Failed to create recipe. Please correct the errors")
    else:
        form = DynamicRecipeForm()

    return render(
        request, "recipes/admin/recipe_form.html", {"form": form,
                                                    "category": category})


# Update recipe
@staff_member_required
def recipe_edit(request, category, pk):
    model = {"breakfast": Breakfast, "lunch": Lunch,
             "snack": Snack}.get(category)
    item = get_object_or_404(model, pk=pk)

    DynamicRecipeForm = modelform_factory(model, fields="__all__")

    if request.method == "POST":
        form = DynamicRecipeForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"{category.title()} recipe updated successfully!")
            return redirect("recipes:recipe_list", category=category)
        messages.error(
            request,
            "Failed to update recipe. Please correct the errors below.")
    else:
        form = DynamicRecipeForm(instance=item)

    return render(
        request, "recipes/admin/recipe_form.html",
        {"form": form, "category": category})


# Delete recipe
@staff_member_required
def recipe_delete(request, category, pk):
    model = {"breakfast": Breakfast, "lunch": Lunch,
             "snack": Snack}.get(category)
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        item.delete()
        messages.success(
            request, f"{category.title()} recipe deleted successfully!")
        return redirect("recipes:recipe_list", category=category)

    return render(
        request, "recipes/admin/recipe_delete.html",
        {"item": item, "category": category})
