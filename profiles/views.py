from django.shortcuts import render,redirect
from . import forms 

# Create your views here.
def add_profile(req):
    if req.method == 'POST':
        profile_form = forms.profileForm(req.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('add_profile')
    else:
        profile_form = forms.profileForm()
    return render(req, 'add_profile.html', {'form': profile_form})