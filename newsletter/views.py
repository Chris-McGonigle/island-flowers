from django.shortcuts import render, redirect

from . models import Subscriber
from django.contrib import messages

def newsletter(request):
    """A view to take email and post to back end"""
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Subscription Successful')
            return redirect('home')
    else:
        form = SubscribersForm()
    
    template = ''
    context = {
        'form': form,
    }
    return render(request, template, context)
