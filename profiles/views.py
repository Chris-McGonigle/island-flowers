from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm
from newsletter.forms import SubscriberForm

from checkout.models import Order


@login_required
def profile(request):
    """
    Function to display user profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Your updated details have been saved")
        else:
            messages.error(
                request,
                "Something went wrong. Please \
                           check and try again.",
            )

    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()

    sub_form = SubscriberForm()
    template = "profiles/profile.html"
    context = {
        "form": form,
        "orders": orders,
        "on_profile_page": True,
        "sub_form": sub_form,
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This ia a past confirmation for order number {order_number}."
            f"A confirmation email was sent on {order.date}."
        ),
    )

    template = "checkout/checkout_success.html"
    context = {"order": order, "from_profile": True}

    return render(request, template, context)
