from django.shortcuts import render, redirect, reverse
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import PostForm


def view_blog(request):
    """View to render main blog page"""

    posts = Post.objects.filter().order_by("-created_on")[:10]

    template = 'blog/blog.html'
    context = {
        'posts': posts
    }

    return render(request, template, context )

@login_required()
def add_post(request):
    """View to add a blog post"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, site owners only!')
        return redirect(reverse('home'))

    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added post!')
            return redirect('blog')
        else:
            messages.error(request, 'Failed to add product. Please \
                           check and try again.')
    
    template = 'blog/add_post.html'
    context = {
        'form': form
    }
    return render(request, template, context)
