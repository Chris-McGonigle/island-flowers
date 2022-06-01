from django.http import HttpResponse


class StripeWH_Handler:
    """Class to handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Method to handle unexpected webhook event"""
        return HttpResponse(
            content=f'Unhandled Webhook received: {event["type"]}', status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """Method to handle the payment intent succeded webhook"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """Method to handle the payment intent failed webhook"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200
        )