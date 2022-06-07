from django.shortcuts import render, redirect

from .models import Subscriber
from .forms import SubscriberForm
from django.contrib import messages


def newsletter(request):
    """A view to take email and post to back end"""
    
    form = SubscriberForm(request.POST or None)
    
    if form.is_valid():
        instance = form.save(commit=False)
        if Subscriber.objects.filter(email=instance.email).exists():
            messages.error(request, 'Sorry, this email already exists in our database.\
                           Please check and try again.')
        else:
            instance.save()
    
    template = 'templates/includes/footer.html'
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
            messages.success(request, '{instance.email} has been removed from our mailing list')
        else:
            messages.error(request, 'Sorry, this email cannot be found in our database.\
                           Please check and try again.')

    template = 'unsubscribe.html'
    context = {
        'form': form,
    }
    return render(request, template, context)