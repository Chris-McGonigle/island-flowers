from django.shortcuts import render
from .models import Post


def view_blog(request):
    """View to render main blog page"""

    posts = Post.objects.filter().order_by("-created_on")[:10]

    template = 'blog/blog.html'
    context = {
        'posts': posts
    }

    return render(request, template, context )
