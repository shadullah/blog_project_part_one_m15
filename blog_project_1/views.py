from django.shortcuts import render
from posts.models import Post
from categories.models import Category

def home(req, category_slug = None):
    data = Post.objects.all()
    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = Post.objects.filter(category = category)
    # print(categories)
    category = Category.objects.all()
    return render(req, 'home2.html', {'data': data,'category': category})

# def home(req, category_slug = None):
#     data = Post.objects.all() 
#     category = Category.objects.get(slug = category_slug)
#  data = Post.objects.filter(category = category)
# categories = Category.objects.all()
# return render(req, 'home2.html', {'data': data,'category': categories})