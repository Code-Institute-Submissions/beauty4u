from products.models import Brand, Category


def product_menu(request):

    """

    Return all brands and categories to show in the menu in alphabetical order

    """

    brands = Brand.objects.all().order_by('brand')
    categories = Category.objects.all().order_by('name')

    context = {
        'brands': brands,
        'categories': categories

    }

    return context
