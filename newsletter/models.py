from django.db import models

class Subscriber(models.Model):
    """Class to hold subscriber details"""
    email = models.EmailField(null=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
