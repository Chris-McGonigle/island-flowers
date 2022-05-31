from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

import stripe

from bag.contexts import bag_contents
from .forms import OrderForm


def checkout(request):
    """
    Method to render out checkout form
    """
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty.")
        return redirect(reverse('products'))

    current_bag = bag_contents(request)
    total = current_bag['grand_total']
    stripe_total = round(total * 100)

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51L5WvdLVFJ15UZcywObrVqbMXMkpoE09q5MvDqZ8bUZGS1tC5Ngn6wYifeIMmWrmWwidM6Ald7gIIFYzff9cCeva00gmabeBiI',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)
