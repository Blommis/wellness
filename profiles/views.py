from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.contrib import messages
# Create your views here.


@login_required
def profile(request):
    """ Shows the users profile and update detail information """
    profile = request.user.userprofile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile was updated successfully!')
    else:
        form = UserProfileForm(instance=profile)
    
    context = {
        'form': form,
    }

    template = 'profiles/profile.html'
    
    return render(request, template, context)

