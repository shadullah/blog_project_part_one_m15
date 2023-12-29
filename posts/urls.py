from django.urls import path 
from . import views

urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
    path('edit_post/<int:id>', views.edit_post, name='edit_post')
]