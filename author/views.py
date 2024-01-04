from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login,update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.contrib.auth.views import LoginView, LogoutView


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
                messages.warning(req, 'Information not correct')
                return redirect('register')
            
    else:
        login_form = AuthenticationForm()
        return render(req, 'register.html', {'form': login_form, 'type': 'Login'})
    

class UserLoginView(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self,form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.warning(self.request, 'Logged info incorrect')
        return super().form_invalid(form)
    
    def get_context_data(data, **kwargs):
        context =super().get_context_data(**kwargs)
        context['type']='login'
        return context
    



    
@login_required
def profile(req):
    data = Post.objects.filter(author = req.user)
    return render(req, 'profile.html', {'data':data})


@login_required
def edit_profile(req):
    if req.method == 'POST':
        profile_form = forms.changUserInfo(req.POST ,instance=req.user)
        if profile_form.is_valid():
            messages.success(req, 'profile updated successfully')
            profile_form.save()
            return redirect('profile')
    else:
        profile_form = forms.RegForm(instance=req.user)
    return render(req, 'edit_profile.html',{'form': profile_form})


def pass_change(req):
    if req.method == 'POST':
        passcngForm = PasswordChangeForm( req.user ,data=req.POST)
        if passcngForm.is_valid():
            messages.success(req, 'Pssword changed successfully')
            update_session_auth_hash(req, passcngForm.user)
            passcngForm.save()
            return redirect('profile')
    else:
        passcngForm = PasswordChangeForm(user=req.user)
    return render(req, 'pass_change.html',{'form': passcngForm})

def user_logout(req):
    logout(req)
    return redirect('user_login')