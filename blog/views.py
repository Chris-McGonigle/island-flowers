from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import PostForm, CommentForm


def view_blog(request):
    """View to render main blog page"""

    posts = Post.objects.filter().order_by("-created_on")[:10]

    template = 'blog/blog.html'
    context = {
        'posts': posts
    }

    return render(request, template, context)

def post_detail(request, post_id):
    """View to render an indvidual blog post page"""

    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter().order_by("-id")

    template = 'blog/post_detail.html'
    context = {
        'post': post,
        'comments': comments,
        'comment_form': CommentForm(),
    }

    return render(request, template, context)


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


@login_required
def edit_post(request, post_id):
    """
    View to update existing post
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, site owners only!')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated post!')
            return redirect(reverse('blog'))
        else:
            messages.error(request, 'Failed to update post. Please \
                           check and try again.')
    else:
        form = PostForm(instance=post)
        messages.info(request, f'You are editing {post.title}')

    template = 'blog/edit_post.html'
    context = {
        'form': form,
        'post': post,
    }

    return render(request, template, context)


@login_required
def delete_post(request, post_id):
    """Method to delete an existing blog post"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, site owners only!')
        return redirect(reverse('home'))

    post = get_object_or_404(Post, pk=post_id)
    post.delete()
    messages.success(request, 'Successfully deleted post!')
    return redirect(reverse('blog'))


@login_required
def add_comment(request, post_id):
    """Method to add comments to a blog post"""
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.all()

    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
            messages.success(request, 'Comment successfully posted!')
            return HttpResponseRedirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, 'Failed to post comment. Please \
                           check and try again.')

    else:
        comment_form = CommentForm()

    template = 'blog/post_detail.html'
    context = {
        'post': post,
        'comments': comments,
        'new-comment': new_comment,
        'comment_form': comment_form,
    }

    return render(request, template, context)


@login_required
def delete_comment(request, comment_id):
    """Method to delete an existing blog post comment"""
    comment = get_object_or_404(Comment, pk=comment_id)

    if not request.user == comment.author:
        messages.error(request, 'Sorry, only comment authors can delete a comment!')
        return redirect(reverse('home'))

    comment.delete()
    messages.success(request, 'Successfully deleted comment')
    return redirect(reverse('blog'))
