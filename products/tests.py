from django.test import TestCase
from .models import Product, Category

class ProductTestCase(TestCase):
    
    
    def setUp(self):
        testCat = Category.objects.create(name='Gaming PCs')
        Product.objects.create(title='computer',brand='hp',sku='123123123',price='999',currency='£', category =testCat, description='words of description',average_rating='4',reviews_count='123',has_sizes=False)
    def test_object_populates_correctly(self):
        testCat = Category.objects.create(name='Gaming PCs')
        product = Product.objects.get(title='computer')
        self.assertEquals(str(product.title),'computer')
        self.assertEquals(str(product.brand),'hp')
        self.assertEquals(int(product.sku),123123123)
        self.assertEquals(int(product.price),999)
        self.assertEquals(str(product.currency),'£')
        self.assertEquals(str(product.category),'Gaming PCs')
        self.assertEquals(str(product.description),'words of description')
        
# Create your tests here.
