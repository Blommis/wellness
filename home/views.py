from django.shortcuts import render, redirect, get_object_or_404
from django.forms import modelform_factory
from django.contrib.admin.views.decorators import staff_member_required
from .models import Event
from datetime import date
from django.contrib import messages
# Create your views here.


def index(request):
    """View to return the index page with upcoming events"""
    events = Event.objects.filter(date__gte=date.today()).order_by('date')
    return render(request, 'home/index.html', {'events': events})


# Main dashbaord site for super user (CRUD)
@staff_member_required
def master_dashboard(request):
    return render(request, "home/master_dashboard.html")


"""
Event CRUD views for staff dashboard.

Provides full create, read, update, and delete functionality for managing
events within the admin dashboard. Only accessible to staff
users via @staff_member_required decorators.
"""


# ADMIN — EVENT LIST
@staff_member_required
def event_list(request):
    items = Event.objects.all().order_by("date")
    return render(request, "home/admin/event_list.html", {"items": items})


# ADMIN — CREATE EVENT
@staff_member_required
def event_create(request):
    EventForm = modelform_factory(Event, fields="__all__")

    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Event created successfully!")
            return redirect("home:event_list")
        else:
            messages.error(request,
                           "Something went wrong. Please check the form.")
    else:
        form = EventForm()

    return render(request, "home/admin/event_form.html", {"form": form})


# ADMIN — EDIT EVENT
@staff_member_required
def event_edit(request, pk):
    item = get_object_or_404(Event, pk=pk)
    EventForm = modelform_factory(Event, fields="__all__")

    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Event updated successfully!")
            return redirect("home:event_list")
        else:
            messages.error(request,
                           "Could not update event. Please review the form.")
    else:
        form = EventForm(instance=item)

    return render(request, "home/admin/event_form.html", {"form": form})


# ADMIN — DELETE EVENT
@staff_member_required
def event_delete(request, pk):
    item = get_object_or_404(Event, pk=pk)

    if request.method == "POST":
        item.delete()
        messages.success(request, "Event deleted successfully!")
        return redirect("home:event_list")

    return render(request, "home/admin/event_delete.html", {"item": item})
