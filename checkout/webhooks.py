from django.conf import settings
from django.http import HttpResponse, HttpRequest
from django.views.decorators.http import require_POST

from checkout.webhook_handler import StripeWH_Handler
from django.views.decorators.csrf import csrf_exempt
import stripe


@require_POST
@csrf_exempt
def webhook(request: HttpRequest):

    """ Set up Stripe credentials """

    wh_secret = settings.STRIPE_WH_SECRET
    stripe.api_key = settings.STRIPE_SECRET_KEY

    """ Retrieve payload and signature from request """
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, wh_secret
        )
    except ValueError as e:
        print(f"Invalid payload: {e}")
        return HttpResponse(status=400)

    except stripe.error.SignatureVerificationError as e:
        print(f" Invalid signature: {e}")
        return HttpResponse(status=400)

    except Exception as e:
        print(f" Unexpected error: {e}")
        return HttpResponse(content=str(e), status=400)

    handler = StripeWH_Handler(request)

    """ Map event types to handler methods """
    event_map = {
        'payment_intent.succeeded': handler.handle_payment_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_payment_intent_failed,
    }
    event_type = event['type']
    event_handler = event_map.get(event_type, handler.handle_event)

    response = event_handler(event)
    return response
