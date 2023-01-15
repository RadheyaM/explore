"""Code source boutique ado"""
from django.http import HttpResponse

class StripeWH_Handler:
    """Handle stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """

        return HttpResponse(
            content=f'Webhook recived: {event["type"]}',
            status=200
        )