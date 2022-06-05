from django.db import models
from django.contrib.auth.models import User
from products.models import Category


class Post(models.Model):
    """Model to create blog posts"""
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=250)
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
