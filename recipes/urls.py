from django.urls import path
from . import views
from .views import delete_review

app_name = 'recipes'

urlpatterns = [
    path('', views.recipes, name='recipes'),
    path('<str:category>/<int:pk>/',
         views.recipe_detail,
         name='recipe_detail'),
    path('review/delete/<int:review_id>/', delete_review, name='delete_review')
]
