from django.shortcuts import render,redirect
from . import forms
# Create your views here.
def add_author(req):
    if req.method == 'POST':
        author_form = forms.authorForm(req.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('add_author')
    else:
        author_form = forms.authorForm()
    return render(req, 'add_author.html',{'form': author_form})