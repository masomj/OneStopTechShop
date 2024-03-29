from django.http import HttpResponse

class stripeWH:
    def __init__(self, request):
        self.request = request
    def handle_event(self,event):
        return HttpResponse(
            content=f'Unhandled Webhook received :{event["type"]}',
            status=200
        )
    def handle_payment_intent_succeeded(self,event):
        return HttpResponse(
            content=f'Successful Payment Intent Webhook received :{event["type"]}',
            status=200
        )
    def handle_payment_intent_failed(self,event):
        return HttpResponse(
            content=f'Webhook received :{event["type"]}',
            status=200
        )
    