from django.urls import path 
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # path('login/', views.user_login, name='user_login'),
    path('login/', views.UserLoginView.as_view(), name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/edit_profile', views.edit_profile, name='edit_profile'),
    path('profile/edit/pass_change/', views.pass_change, name='passchange')
]
