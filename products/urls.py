from django.contrib import admin
from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.supplements, name='supplements'),
    path('<int:pk>/', views.supplement_detail, name='supplement_detail')
]