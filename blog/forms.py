from django.forms import ModelForm
from .models import Post, Comment


class PostForm(ModelForm):
    """
    Form to allow site owner to create a new blog post
    """
    class Meta:
        model = Post
        fields = ['category', 'title', 'body', 'image']


class CommentForm(ModelForm):
    """Form to handle user comments"""
    class Meta:
        model = Comment
        fields = ('body',)