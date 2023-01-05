from django.test import TestCase
from .models import Product, Category, CategoryParent

class ProductModelsTestCase(TestCase):
    
    
    def setUp(self):
        parent_category = CategoryParent.objects.create(name='Computers')
        testCat = Category.objects.create(name='Gaming PCs', parentCategory = parent_category)
        Product.objects.create(title='computer',brand='hp',sku='123123123',price='999',currency='£', category =testCat, description='words of description',average_rating='4',reviews_count='123',has_sizes=False)
    
    def test_object_populates_correctly(self):
        product = Product.objects.get(title='computer')
        self.assertEquals(str(product.title),'computer')
        self.assertEquals(str(product.brand),'hp')
        self.assertEquals(int(product.sku),123123123)
        self.assertEquals(int(product.price),999)
        self.assertEquals(str(product.currency),'£')
        self.assertEquals(str(product.category),'Gaming PCs')
        self.assertEquals(str(product.description),'words of description')
        
    def test_category_object_populates(self):
        
        cat = Category.objects.get(name = 'Gaming PCs')
        self.assertEquals(str(cat.name),'Gaming PCs')
        self.assertAlmostEquals(str(cat.parentCategory),'Computers')
    def test_parentCategory_object_populates(self):
        cat = CategoryParent.objects.get(name='Computers')
        self.assertEquals(str(cat.name),'Computers')
