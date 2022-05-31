from django.db.models.signals import post_save, post_delete
from django.dispath import receiver

from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Method to update lineitem order total on newly
    created or updated lines
    """
    instance.order.update_total()