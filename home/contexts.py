from products.models import Category, CategoryParent


def categories_processor(request):
    categories = Category.objects.all()
    parent_categories = CategoryParent.objects.all()
    return {
        'categories':categories,
        'parent_categories':parent_categories
    }   