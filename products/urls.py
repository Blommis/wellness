from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('supplements/', views.supplements, name='supplements'),
    path('<int:pk>/', views.supplement_detail, name='supplement_detail'),
    path('mealplans/', views.view_mealplan, name='view_mealplan'),
    path('search/', views.search_results, name='search_results'),
    path('supplement/<int:pk>/image/', views.supplement_image,
         name='supplement_image'),

    path("dashboard/supplements/", views.supplement_dashboard,
         name="supplement_dashboard"),
    path("dashboard/supplements/list/", views.supplement_list,
         name="supplement_list"),
    path("dashboard/supplements/add/", views.supplement_create,
         name="supplement_create"),
    path("dashboard/supplements/<int:pk>/edit/", views.supplement_edit,
         name="supplement_edit"),
    path("dashboard/supplements/<int:pk>/delete/", views.supplement_delete,
         name="supplement_delete"),
]
