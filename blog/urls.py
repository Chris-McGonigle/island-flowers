from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_blog, name="blog"),
    path('add_post/', views.add_post, name="add_post"),
    path('edit/<int:post_id>/', views.edit_post, name="edit_post"),
]
