from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_blog, name="blog"),
    path('add_post/', views.add_post, name="add_post"),
    path('edit/<int:post_id>/', views.edit_post, name="edit_post"),
    path('delete/<int:post_id>/', views.delete_post, name="delete_post"),
]
