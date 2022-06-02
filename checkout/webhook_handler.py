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
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info
        
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.data.charges[0].amount / 100, 2)

        # Clean up shipping details data for empty fields
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=shipping_details.email,
                    phone_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.country,
                    postcode__iexact=shipping_details.postcode,
                    town_or_city__iexact=shipping_details.city,
                    street_address1__iexact=shipping_details.line1,
                    street_address2__iexact=shipping_details.line2,
                    county__iexact=shipping_details.state,
                    grand_total__iexact=grand_total,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt =+ 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database', status=200)
        else:
            order = None
            try:
                order = order.Objects,create(
                    full_name=shipping_details.name,
                    email=shipping_details.email,
                    phone_number=shipping_details.phone,
                    country=shipping_details.country,
                    postcode=shipping_details.postcode,
                    town_or_city=shipping_details.city,
                    street_address1=shipping_details.line1,
                    street_address2=shipping_details.line2,
                    county=shipping_details.state,
                        )
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=f'Webhook received: {event["type"]} | ERROR: {e}', status=500)  
        return HttpResponse(content=f'Webhook received: {event["type"]} | SUCCESS: Created order in database', status=200)


    def handle_payment_intent_payment_failed(self, event):
        """Method to handle the payment intent failed webhook"""
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200
        )