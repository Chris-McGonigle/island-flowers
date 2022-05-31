from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem


@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Method to update lineitem order total on newly
    created or updated lines
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def delete_on_save(sender, instance, **kwargs):
    """
    Method to update lineitem order total after line delete
    """
    instance.order.update_total()
