from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.db.models.functions import Lower
from .models import Product, Category, CategoryParent
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required

def staff_required(login_url = None):
    return user_passes_test(lambda u: u.is_staff,login_url=login_url)


from reviews.models import review
from .forms import editProductForm, editCategoryForm
import random



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
    all_reviews = review.objects.filter(product = product)
    print(all_reviews)
    if all_reviews.count() > 3:
        reviews = random.sample(all_reviews, 3)
    else:
        reviews = all_reviews
    
    context={
        'product':product,
        'categories':all_categories,
        'parent_categories':parent_categories,
        'reviews':reviews
        
        
    }
    return render(request,'productInfo.html',context)


@staff_required(login_url="/accounts/login")
def editCategory(request):

    return render()
@staff_required(login_url="/accounts/login")
def createCategory(request):

    return render()
@staff_required(login_url="/accounts/login")
def deleteCategory(request):
     
    return render()
@staff_required(login_url="/accounts/login")
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
    return render(request, 'addProduct.html', context)

@staff_required(login_url="/accounts/login")
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
@staff_required(login_url="/accounts/login")
def deleteProduct(request,product_id):
    product = get_object_or_404(Product, pk = product_id)
    product.delete()
    print('deleted')
    return products(request)

@staff_required(login_url="/accounts/login")
def admin(request):

    return render(request, 'admin.html')
