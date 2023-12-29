from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def add_post(req):
    if req.method == 'POST':
        post_form = forms.postForm(req.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
    else:
        post_form = forms.postForm()
    return render(req, 'add_post.html', {'form': post_form})


def edit_post(req, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.postForm(instance=post)
    
    if req.method == 'POST':
        post_form = forms.postForm(req.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('/')
    return render(req, 'add_post.html', {'form': post_form})

def delete_post(req, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('/')