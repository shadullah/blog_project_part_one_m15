from django.urls import path 
from . import views

urlpatterns = [
    path('add_post/', views.add_post, name='add_post'),
    path('add_post/', views.addPostCreatView.as_view(), name='add_post'),
    # path('edit_post/<int:id>', views.edit_post, name='edit_post'),
    path('edit_post/<int:id>', views.editClassView.as_view(), name='edit_post'),
    # path('delete/<int:id>', views.delete_post, name='delete_post')
    path('delete/<int:id>', views.deleteClassView.as_view(), name='delete_post'),
    # path('detais/<int:pk>/', views.detailsPageClass, name = 'details_page') id and pk are same
    path('detalis/<int:id>/', views.detailsPageClass.as_view(), name = 'details_page')
]