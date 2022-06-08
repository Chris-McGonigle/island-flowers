from django.shortcuts import render
from blog.models import Post
from newsletter.forms import SubscriberForm

def index(request):
    """View to render the home index page"""

    posts = Post.objects.filter().order_by("-id")[:3]

    sub_form = SubscriberForm()

    context = {
        'posts': posts,
        'sub_form': sub_form,
    }
    return render(request, 'home/index.html', context)
