from django.urls import path
from . import views
urlpatterns = [
path('', views.products, name='products'),
path('<product_id>', views.productInfo, name='productInfo'),
path('<product_id>/',views.editProduct, name='editProduct'),
path('<product_id>/delete',views.deleteProduct, name='deleteProduct'),
path('/createProduct',views.createProduct,name='createProduct')
]