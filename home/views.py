from django.shortcuts import render
from blog.models import Post

def index(request):
    """View to render the home index page"""

    posts = Post.objects.filter().order_by("-id")[:3]

    context = {
        'posts':posts
    }
    return render(request, 'home/index.html', context)
