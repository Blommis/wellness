from django.urls import path
from . import views

app_name = "home"

urlpatterns = [
    path('', views.index, name='index'),
    path("dashboard/", views.master_dashboard, name="master_dashboard"),
    # EVENT CRUD
    path("dashboard/events/", views.event_list, name="event_list"),
    path("dashboard/events/add/", views.event_create, name="event_create"),
    path("dashboard/events/<int:pk>/edit/", views.event_edit,
         name="event_edit"),
    path("dashboard/events/<int:pk>/delete/", views.event_delete,
         name="event_delete"),
]
