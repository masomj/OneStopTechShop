from django.urls import path
from . import views
urlpatterns = [
path('', views.products, name='products'), #products
path('<product_id>', views.productInfo, name='productInfo'), #product info
path('admin/editproduct/<product_id>',views.editProduct, name='editProduct'), #edit product info
path('admin/selectProduct', views.selectProduct, name='selectProduct'),
path('admin/delete/<product_id>',views.deleteProduct, name='deleteProduct'), #delete product
path('admin/createProduct',views.createProduct,name='createProduct'), #create new product
path('admin/updateCategory',views.editCategory,name='updateCategory'),
path('admin/createCategory',views.createCategory,name='createCategory'),
path('admin/createParentCategory',views.createParentCategory,name='createParentCategory'),
path('admin/updateCategory/<category_id>',views.editCategoryDetails,name='editCategoryDetails'),
path('admin/updateParentCategory',views.editParentCategory ,name='updateParentCategory'),
path('admin/updateParentCategory/<category_id>',views.editParentCategoryDetails ,name='editParentCategoryDetails'),#update Parent Category
path('admin/',views.admin ,name="admin") #view admin page
]