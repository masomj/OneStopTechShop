from django.urls import path
from . import views
from .webhooks import webhook
urlpatterns = [
path('', views.checkout, name='checkout'),
path('checkout/pay', views.pay, name='pay'),
path('checkout/completed/<order_id>',views.completedCheckout, name="completedCheckout"),
path('wh/', webhook ,name='webhook')


]