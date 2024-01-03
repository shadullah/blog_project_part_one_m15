from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(req):
    if req.method == 'POST':
        reg_form = forms.RegForm(req.POST)
        if reg_form.is_valid():
            messages.success(req, 'account created successfully')
            reg_form.save()
            return redirect('register')
    else:
        reg_form = forms.RegForm()
    return render(req, 'register.html',{'form': reg_form, 'type': 'Register'})

def user_login(req):
    if req.method =='POST':
        login_form = AuthenticationForm(req, req.POST)
        if login_form.is_valid():
            user_name = login_form.cleaned_data['username']
            user_pass = login_form.cleaned_data['password']
            user = authenticate(username= user_name, password = user_pass)
            if user is not None:
                messages.success(req, 'Logged in successfully')
                login(req, user)
                return redirect('profile')
            else:
                messages.warning(req, 'login information not correct')
                return redirect('register')
            
    else:
        login_form = AuthenticationForm()
        return render(req, 'register.html', {'form': login_form, 'type': 'Login'})
    
@login_required
def profile(req):
    if req.method == 'POST':
        profile_form = forms.changUserInfo(req.POST ,instance=req.user)
        if profile_form.is_valid():
            messages.success(req, 'profile updated successfully')
            profile_form.save()
            return redirect('register')
    else:
        profile_form = forms.RegForm(instance=req.user)
    return render(req, 'profile.html',{'form': profile_form})