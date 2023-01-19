from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.db.models.functions import Lower
from .models import Product, Category, CategoryParent
from django.db.models import Q
from django.forms import ModelForm, Textarea
from django.contrib.auth.decorators import login_required

# Create your views here.

def products(request):
    products = Product.objects.all()
    categories = None
    sort = None
    direction = None
    query = None
    all_categories = Category.objects.all()
    parent_categories = CategoryParent.objects.all()
    
    
    if request.GET:
        
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            
            if sortkey == 'name': #alphabetical name sort
                sortkey == 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
                                             
            if sortkey == 'category': #alphabetical category sort
                sortkey = 'category__name'
                
            if 'direction' in request.GET: #direction sort
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
                    
        
        if 'category' in request.GET: #category filtering
            categories = request.GET['category'].split(',') 
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'query' in request.GET:
            query = request.GET['query']
            queries = Q(title__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)
            
    current_sorting = f'{sort}_{direction}'
    
    
    context={
        'products':products,
        'selected_categories':categories,
        'current_sorting':current_sorting,
        'query':query,
        'categories':all_categories,
        'parent_categories':parent_categories,
        
    }
    

    return render(request,'products.html',context)

def productInfo(request,product_id):
    product = get_object_or_404(Product, pk = product_id)
    all_categories = Category.objects.all()
    parent_categories = CategoryParent.objects.all()
    context={
        'product':product,
        'categories':all_categories,
        'parent_categories':parent_categories,
    }
    return render(request,'productInfo.html',context)

class editProductForm(ModelForm):
    class Meta:
        model = Product
        fields =['title','brand','sku','price','images','category','description','average_rating','reviews_count','has_sizes']
        widgets = {
            'description': Textarea(attrs={'cols': 80, 'rows': 15}),
            'title':Textarea(attrs={'cols': 40, 'rows': 1}),
            'images':Textarea(attrs={'cols': 80, 'rows': 1}),
        }

class editProductForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'parentCategory']

def editCategory(request):

    return render()

def createCategory(request):

    return render()

def deleteCategory(request):
     
    return render()

def createProduct(request):
    all_categories = Category.objects.all()
    parent_categories = CategoryParent.objects.all()
    form = editProductForm()
   
    if request.method=='POST':

        newProduct=editProductForm(request.POST)

        if newProduct.is_valid():
            newProduct.save()
        else:
            print('not valid')
        return products(request)
        
    context={
        'categories':all_categories,
        'parent_categories':parent_categories,
        'form':form
    }
    return render(request, 'addProduct.html',context)

@login_required
def editProduct(request, product_id):
    product = get_object_or_404(Product, pk = product_id)
    all_categories = Category.objects.all()
    parent_categories = CategoryParent.objects.all()
    form = editProductForm(instance=product)

    if request.method == 'POST':
        edits = editProductForm(request.POST, instance=product)
        
        if edits.is_valid():
            edits.save()
        else:
            print('not valid')
        return products(request)

    context={
        'product':product,
        'categories':all_categories,
        'parent_categories':parent_categories,
        'form':form
    }
    return render(request,'editProduct.html',context)

def deleteProduct(request,product_id):
    product = get_object_or_404(Product, pk = product_id)
    product.delete()
    print('deleted')
    return products(request)


def admin(request):

    return render(request, 'admin.html')
