from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from .models import Subscriber
from .forms import SubscriberForm
from django.contrib import messages


def newsletter(request):
    """A view to take email and post to back end"""
    
    form = SubscriberForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        if Subscriber.objects.filter(email=instance.email).exists():
            messages.error(request, f'Sorry, {instance.email} already exists in our database.\
                           Please check and try again.')
        else:
            instance.save()
            messages.success(request, f'Congratulations! {instance.email} has been added to our mailing list')
            return redirect('home')
    
    template = 'home/index.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


def unsubscribe(request):
    """A view to handle unsubcribing users"""
    form = SubscriberForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if Subscriber.objects.filter(email=instance.email).exists():
            Subscriber.objects.filter(email=instance.email).delete()
            messages.success(request, f'{instance.email} has been removed from our mailing list')
        else:
            messages.error(request, f'Sorry, {instance.email} cannot be found in our database.\
                           Please check and try again.')

    template = 'unsubscribe.html'
    context = {
        'form': form,
    }
    return render(request, template, context)