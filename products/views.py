from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.db.models.functions import Lower
from .models import Product, Category, CategoryParent
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from reviews.models import review
from .forms import editProductForm, editCategoryForm, categorySelector, editParentCategoryForm, parentCategorySelector
import random
def staff_required(login_url = None):
    return user_passes_test(lambda u: u.is_staff,login_url=login_url)






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
def editCategoryDetails(request,category_id):
    if request.method == 'POST':
        category_to_edit = get_object_or_404(Category, pk=category_id)
        edited_form = editCategoryForm(request.POST, instance=category_to_edit)
        if edited_form.is_valid():
            edited_form.save()
        
        return redirect(reverse('products'))

@staff_required(login_url="/accounts/login")
def editCategory(request):

    if request.method == 'POST': 
        if 'category' in request.POST:
            selected_category = request.POST['category']
            category_to_edit = get_object_or_404(Category, pk=selected_category)
            form=editCategoryForm(instance=category_to_edit)
            context ={
            'form':form,
            'selected_category':category_to_edit
            
        } 
            return render(request,'editCategoryDetails.html', context)

    else:
            category_selector = categorySelector()
            context ={
            'category_selector':category_selector,
            
        }
    
    
    return render(request, 'editCategory.html', context)

@staff_required(login_url="/accounts/login")
def editParentCategoryDetails(request,category_id):
    if request.method == 'POST':
        category_to_edit = get_object_or_404(CategoryParent, pk=category_id)
        edited_form = editParentCategoryForm(request.POST, instance=category_to_edit)
        if edited_form.is_valid():
            edited_form.save()
        
        return redirect(reverse('products'))

@staff_required(login_url="/accounts/login")
def editParentCategory(request):
    if request.method == 'POST': 
        if 'parentCategory' in request.POST:
            selected_category = request.POST['parentCategory']
            category_to_edit = get_object_or_404(CategoryParent, pk=selected_category)
            form=editParentCategoryForm(instance=category_to_edit)
            context ={
            'form':form,
            'selected_category':category_to_edit
            
        } 
            return render(request,'editParentCategoryDetails.html', context)
        elif 'name' in request.POST:
                edited_form = editParentCategoryForm(request.POST)
                print(category_to_edit)
                if edited_form.is_valid():
                    edited_form.save()
                    print(edited_form)
                    print('saved')
                    return redirect(reverse('admin'))  
    else:
        category_selector = parentCategorySelector()
        context ={
        'category_selector':category_selector,
        
    }
    return render(request,'editParentcategory.html', context )


@staff_required(login_url="/accounts/login")
def createParentCategory(request):
    form = editParentCategoryForm()
    if request.method == 'POST':
        newCat = editParentCategoryForm(request.POST)
        if newCat.is_valid():
            newCat.save()
            messages.success(request, 'Parent Category Added')
            return redirect(reverse('admin'))
    context= {
       'form':form
    }
    return render(request, 'addParentCategory.html', context)



@staff_required(login_url="/accounts/login")
def createCategory(request):
    form = editCategoryForm()
    if request.method == 'POST':
        newCat = editCategoryForm(request.POST)
        if newCat.is_valid():
            newCat.save()
            messages.success(request, 'Category Added')
            return redirect(reverse('admin'))
    context= {
       'form':form
    }
    return render(request, 'addCategory.html', context)

@staff_required(login_url="/accounts/login")
def createProduct(request):
    all_categories = Category.objects.all()
    parent_categories = CategoryParent.objects.all()
    form = editProductForm()
   
    if request.method=='POST':

        newProduct=editProductForm(request.POST)

        if newProduct.is_valid():
            newProduct.save()
            messages.success(request, 'Product Added')
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
def selectProduct(request):
    products = Product.objects.all() 
    context={
    'products':products
}

    return render( request, 'selectProduct.html',context)

@staff_required(login_url="/accounts/login")
def editProduct(request, product_id):
    if request.method == 'POST':
        if 'title' in request.POST:
            product = get_object_or_404(Product, pk = product_id)
            edits = editProductForm(request.POST, instance=product)
            if edits.is_valid():
                edits.save()
                print(product)
                print('saved')
                messages.success(request, 'Product Changed')
                return redirect(reverse('admin'))
            else:
                messages.warning(request,'Form Not valid')
                return redirect(reverse('editProduct'))
        elif 'product' in request.POST:
            product_id = request.POST['product']
            product = get_object_or_404(Product, pk = product_id)
            all_categories = Category.objects.all()
            parent_categories = CategoryParent.objects.all()
            form = editProductForm(instance=product)
            context={
            'product':product,
            'categories':all_categories,
            'parent_categories':parent_categories,
            'form':form
            }
            return render(request,'editProduct.html',context)
    else:   
        product = get_object_or_404(Product, pk = product_id)
        all_categories = Category.objects.all()
        parent_categories = CategoryParent.objects.all()
        form = editProductForm(instance=product)
        context={
            'product':product,
            'categories':all_categories,
            'parent_categories':parent_categories,
            'form':form
            }
        return render(request,'editProduct.html',context)
    return redirect(reverse('products'))
@staff_required(login_url="/accounts/login")
def deleteProduct(request,product_id):
    product = get_object_or_404(Product, pk = product_id)
    product.delete()
    messages.success(request,'Product Deleted')
    return products(request)

@staff_required(login_url="/accounts/login")
def admin(request):

    return render(request, 'admin.html')
