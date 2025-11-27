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

    # Main Products Dashboard
    path("dashboard/products/", views.products_dashboard,
         name="products_dashboard"),

    # supplement CRUD
    path("dashboard/products/supplements/", views.supplement_list,
         name="supplement_list"),
    path("dashboard/products/supplements/add/", views.supplement_create,
         name="supplement_create"),
    path("dashboard/products/supplements/<int:pk>/edit/",
         views.supplement_edit,
         name="supplement_edit"),
    path("dashboard/products/supplements/<int:pk>/delete/",
         views.supplement_delete,
         name="supplement_delete"),

    # Meal Plans CRUD
    path("dashboard/products/mealplans/",
         views.mealplan_list, name="mealplan_list"),
    path("dashboard/products/mealplans/add/",
         views.mealplan_create, name="mealplan_create"),
    path("dashboard/products/mealplans/<int:pk>/edit/",
         views.mealplan_edit, name="mealplan_edit"),
    path("dashboard/products/mealplans/<int:pk>/delete/",
         views.mealplan_delete, name="mealplan_delete"),
]
