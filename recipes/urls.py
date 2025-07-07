from django.urls import path
from . import views
urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('<str:category>/<int:pk>/', views.recipe_detail, name='recipe_detail')
]