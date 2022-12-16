from django.urls import path
from . import views
urlpatterns = [
path('', views.products, name='products'),
path('<product_id>', views.productInfo, name='productInfo'),
path('<product_id>/',views.editProduct, name='editProduct'),
path('createProduct/',views.createProduct,name='createProduct')
]