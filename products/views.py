from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
import random
from django.db.models import Q
from .models import Product, Brand, Category

# Create your views here.
def all_products(request):
    """ A view that returns the index page """
    products = Product.objects.all()
    brandList = Brand.objects.all()
    query = None
    brand = None
    sort = None
    direction = None
    selectedBrand = None
 
    #Get Featured Products 
    featured_products = products.filter(featured_product=True)



    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sort == "price":
                sortkey = 'price'
            if sort == "rating":
                sortkey = 'rating'    
                sortkey = f'-{sortkey}'
                # By Default - sort by lowest to highest
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == "dsc":
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)


        if 'brand' in request.GET:
            brand = request.GET['brand']
            if not brand:
                messages.error(request, "Nothing Found!")
                return redirect(reverse('products'))
            products = products.filter(brand_id__in=brand)
            selectedBrand = brandList.filter(id=brand)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not search for anything!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)


    context = {
        'products': products,
        'featured_products': featured_products,
        'query': query,
        'brandList': brandList,
        'brand': brand, #Output brand selected to top of page
        'selectedBrand': selectedBrand,

    }

    return render(request, 'products/products.html',context)

def product_detail (request, product_id):
    """ A view that returns a single product template - Also renders related products from that brand """
    products = Product.objects.all()
    product = get_object_or_404(Product, pk=product_id)
    related_products = products.filter(brand=product.brand)

    context = {
        'product': product,
        'related_products': related_products
       

    }

    return render(request, 'products/product_detail.html',context)