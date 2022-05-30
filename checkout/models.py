import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product


class Order(models.Model):
    """Class to hold complete order details"""
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, blank=False, default=0)
                                      
    def _generate_order_number(self):
        """Method to generate a unique order number"""
        return uuid.uuid4().hex.upper()


    def save(self, *args, **kwargs):
        """
        Override default save method to set order number
        if it hasn't already been set
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
            super().save(*args, **kwargs)



class OrderLineItem(models.Model):
    """Class to hold indiviudal order items"""
    order = models.ForeignKey(Order, null=False, blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2,
                                         null=False, blank=False,
                                         editable=False)
