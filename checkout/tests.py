from django.test import TestCase
from .models import order, orderItem
from products.models import Product, Category, CategoryParent

# Create your tests here.

class checkoutModelsTestCase(TestCase):
    
    
    def setUp(self):
        parent_category = CategoryParent.objects.create(name='Computers')
        testCat = Category.objects.create(name='Gaming PCs', parentCategory = parent_category)
        testProduct = Product.objects.create(title='computer',brand='hp',sku='123123123',price='999',currency='£', category =testCat, description='words of description',average_rating='4',reviews_count='123',has_sizes=False)

        testOrder = order.objects.create(
            order_number='123',
            full_name="John Deer",
            email="email@email.com", 
            phone_number="07777777777",
            country="Skippistan", 
            postcode='ab122cd',
            town="roach motel",
            city="paradise",
            street_name="newark", 
            house_number="21",
            payed=False

        )
        testItem = orderItem.objects.create(
            order = testOrder, product = testProduct, quantity = 1
        )
        
        
    def test_order_object_populates_correctly(self):
        
        test_order = order.objects.get(order_number='123')
        self.assertEquals(str(test_order.order_number),'123')
        self.assertEquals(str(test_order.full_name),'John Deer')
        self.assertEquals(str(test_order.email),'email@email.com')
        self.assertEquals(str(test_order.phone_number),'07777777777')
        self.assertEquals(str(test_order.country),'Skippistan')
        self.assertEquals(str(test_order.postcode),'ab122cd')
        self.assertEquals(str(test_order.town),'roach motel')
        self.assertEquals(str(test_order.city),'paradise')
        self.assertEquals(str(test_order.street_name),'newark')
        self.assertEquals(str(test_order.house_number),'21')
        self.assertEquals(int(test_order.order_total),999)
        self.assertEquals(int(test_order.payment_due),999)

          
        
    