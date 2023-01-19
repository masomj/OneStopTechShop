from django.http import HttpResponse
from django.conf import settings
import stripe
from checkout.webhookhandler import stripeWH
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt


@require_POST
@csrf_exempt
def webhook(request):
    """Direct from https://stripe.com/docs/webhooks """
    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY
    
    payload = request.body
    sig_header=request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Event.construct_from(
        payload, sig_header, wh_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(status=400, content=e)
    
    handler = stripeWH(request)
    
    event_map = {
        'payment_intent.succeeded':handler.handle_payment_intent_succeeded,
        'payment_intent.failed':handler.handle_payment_intent_failed
    }
    
    event_type = event['type']
    
    event_handler = event_map.get(event_type, handler.handle_event)
    response = event_handler(event)
    return response
    
    
    
    