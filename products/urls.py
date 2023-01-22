from django.urls import path
from . import views
urlpatterns = [
path('', views.products, name='products'), #products
path('<product_id>', views.productInfo, name='productInfo'), #product info
path('admin/editproduct/<product_id>',views.editProduct, name='editProduct'), #edit product info
path('admin/delete/<product_id>',views.deleteProduct, name='deleteProduct'), #delete product
path('admin/createProduct',views.createProduct,name='createProduct'), #create new product
path('admin/updateCategory',views.editCategory,name='updateCategory'), #update Category
path('admin/',views.admin ,name="admin") #view admin page
]