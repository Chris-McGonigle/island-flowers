from django.forms import ModelForm
from .models import Post, Comment
from crispy_forms.helper import FormHelper


class PostForm(ModelForm):
    """
    Form to allow site owner to create a new blog post
    """

    class Meta:
        model = Post
        fields = ["category", "title", "body", "image"]


class CommentForm(ModelForm):
    """Form to handle user comments"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.fields['body'].label = False

    class Meta:
        model = Comment
        fields = ("body",)
