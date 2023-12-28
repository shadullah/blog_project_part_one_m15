from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def add_category(req):
    if req.method == 'POST':
        category_form = forms.categoryForm(req.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('add_category')
    else:
        category_form = forms.categoryForm()
    return render(req, 'add_category.html', {'form': category_form})