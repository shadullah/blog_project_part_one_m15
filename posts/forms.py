from django import forms 
from . models import Post,Comment

class postForm(forms.ModelForm):
    class Meta: 
        model = Post
        # fields = '__all__',
        # fields = ['name', 'bio']
        exclude = ['author']


class CmntForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ['name', 'email', 'body']

# class CommentForm(forms.ModelForm):
#     class Meta: 
#         model = Comment
#         fields = ['name', 'email', 'body']