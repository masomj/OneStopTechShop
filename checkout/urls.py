from django.urls import path
from . import views
from . import webhooks
urlpatterns = [
path('', views.checkout, name='checkout'),
path('checkout/pay', views.pay, name='pay'),
path('wh/', webhooks ,name='webhook')


]