from django.urls import path
from . import views
from .views import delete_review

app_name = 'recipes'

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('<str:category>/<int:pk>/',
         views.recipe_detail,
         name='recipe_detail'),
    path('review/delete/<int:review_id>/', delete_review, name='delete_review'),

    path('dashboard/recipes/', views.recipe_dashboard, name='recipe_dashboard'),
    path('dashboard/recipes/<str:category>/', views.recipe_list, name='recipe_list'),
    path('dashboard/recipes/<str:category>/add/', views.recipe_create, name='recipe_create'),
    path('dashboard/recipes/<str:category>/<int:pk>/edit/', views.recipe_edit, name='recipe_edit'),
    path('dashboard/recipes/<str:category>/<int:pk>/delete/', views.recipe_delete, name='recipe_delete'),


]
