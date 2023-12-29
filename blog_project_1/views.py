from django.shortcuts import render
from posts.models import Post

def home(req):
    data = Post.objects.all()
    print(data)
    return render(req, 'home2.html', {'data': data})