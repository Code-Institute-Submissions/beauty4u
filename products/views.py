from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
import random
from django.db.models import Q
from .models import Product, Brand, Category, Review
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.
def all_products(request):
    """ A view that returns the index page """
    products = Product.objects.all()
    brandList = Brand.objects.all()
    query = None
    brand = None
    sort = None
    category = None
    direction = None
    selectedBrand = None
    sale = None
 
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
        
        if 'category' in request.GET:
            category= request.GET['category']
            if not category:
                messages.error(request, "Nothing Found!")
                return redirect(reverse('products'))
            products = products.filter(category__name=category)
            

        if 'brand' in request.GET:
            brand = request.GET['brand']
            if not brand:
                messages.error(request, "Nothing Found!")
                return redirect(reverse('products'))
            products = products.filter(brand__brand=brand)


        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You did not search for anything!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

        if 'sale' in request.GET:
            sale = request.GET['sale']
           # if sale == "True":
            if sale == "true":
               products = products.filter(sale_price__gt = 0)

        # Only show in stock products
        products = products.filter(in_stock=True)

        # If there is any filtering, render results template
        if 'sale' in request.GET or 'q' in request.GET or 'brand' in request.GET or 'sort' in request.GET or 'category' in request.GET:
            context = {
            'products': products,
            'featured_products': featured_products,
            'query': query,
            'brand': brand, #Output brand selected to top of page
            'category': category,
            'sale': sale,
            'query': query,
            }



        return render(request, 'products/results.html',context)

    #Only show products marked in stock
    products = products.filter(in_stock=True)


    #Shampoo Products 
    hair_products = products.filter(category__name="Shampoo").order_by('-id')[:4]
    conditoner_products = products.filter(category__name="Conditioner").order_by('-id')[:4]
    skin_products = products.filter(category__name="Skin").order_by('-id')[:4]


    context = {
        'products': products,
        'featured_products': featured_products,
        'query': query,
        'brandList': brandList,
        'brand': brand, #Output brand selected to top of page
        'selectedBrand': selectedBrand,
        'hair_products':  hair_products,
        'conditoner_products': conditoner_products,
        'skin_products': skin_products,
     

    }

    return render(request, 'products/products.html',context)

def product_detail (request, product_id):

    """ A view that returns a single product template - Also renders related products from that brand """
    products = Product.objects.all()
    product = get_object_or_404(Product, pk=product_id)
    related_products = products.filter(brand=product.brand)
    reviews = Review.objects.filter(product=product_id).order_by('-id')
    total_reviews = Review.objects.filter(product=product_id).count()
    total_score = 0
    avg_score = 0
    if total_reviews != 0:
        for review in reviews:
            total_score += review.score 
        avg_score = total_score / total_reviews


    review_check = Review.objects.filter(added_by=request.user.username, product=product)
    if len(review_check) == 0:
        review_check_complete = 0
    else:
        review_check_complete = 1

    context = {
        'product': product,
        'related_products': related_products,
        'reviews': reviews,
        'review_check_complete': review_check_complete,
        'avg_score': round(avg_score),
        'total_reviews': total_reviews

    }

    return render(request, 'products/product_detail.html', context)

@require_POST
def add_review(request): 

    review = request.POST.get('review')
    product_id = request.POST.get('product_id')
    username = request.user.username
    score = request.POST.get('rating')

    product = Product.objects.get(pk=product_id)

    Review.objects.get_or_create(product=product, review=review, added_by=username, score=score)

    result = {
        'review': review,
        'score': score,
        'username': username,
    }

    return JsonResponse(result)   