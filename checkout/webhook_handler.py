from django.http import HttpResponse

class StripeWH_Handler:

    def __init__ (self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(content=f'webhook received: { event["type"]}', 
        status=200)    


    def handle_payment_intent_succeeded(self, event):
        """
        Handle payment intent succeeded webhook from Stripe 
        """
        return HttpResponse(content=f'webhook received: { event["type"]}', 
        status=200)    

    def handle_payment_intent_failed(self, event):
        """
        Handle payment intent succeeded webhook from Stripe 
        """
        return HttpResponse(content=f'webhook received: { event["type"]}', 
        status=200)    


