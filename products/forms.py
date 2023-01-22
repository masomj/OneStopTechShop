from .models import Product, Category, CategoryParent
from django.forms import ModelForm, Textarea, FileField

class editProductForm(ModelForm):
    class Meta:
        model = Product
        fields =['title','brand','sku','price','image_url', 'image_file','category','description','average_rating','reviews_count','has_sizes']
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 15}),
            'title':Textarea(attrs={'cols': 40, 'rows': 1}),
            'image_url':Textarea(attrs={'cols': 80, 'rows': 1}),
            
        }


class editCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'parentCategory', ]

class editParentCategoryForm(ModelForm):
    class Meta:
        model= CategoryParent
        fields= ['name']

class categorySelector(ModelForm):
    class Meta:
        model = Product
        fields =['category']

class parentCategorySelector(ModelForm):
    class Meta:
        model = Category
        fields = ['parentCategory']