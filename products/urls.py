from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('supplements/', views.supplements, name='supplements'),
    path('<int:pk>/', views.supplement_detail, name='supplement_detail'),
    path('mealplans/', views.view_mealplan, name='view_mealplan'),
    path('search/', views.search_results, name='search_results'),
    path('supplement/<int:pk>/image/', views.supplement_image, name='supplement_image')
]
