from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,Http404

# Create your views here.

products={
    1:{'name' : 'laptop', 'price' : 1500},
    2:{'name' : 'charger', 'price' : 1100},
    3:{'name' : 'C', 'price' : 150},
}

def home(request):
    return HttpResponse("<h1>Welcome to Product Store</h1>")

def all_products(request):
    product_items={product['name']: product['price'] for product in products.values() }
    return JsonResponse(product_items)

#dynamic url
def products_details_by_id(requestm product_id):
    product = products.get(product_id)
    if product:
        return HttpResponse(
            f"<h1>Product Details</h1>"
            f"<p>Na me: {product['name</p>"
            f"<p>Product Details</p>"

        )
    else:
        raise Http404(f"Product with ID {product_id} not found")

#for string
def products_details_by_id(request, product_name):
    for product in products.values():
        if product['name']==product_name:
            return HttpResponse(
                f"<h1> Product Details</h1>"
                f"<p> Name: {product['name']}</p>"
                f"<p> Name: {product['price']}</p>"
            )
        return HttpResponse(f"<h1>Product with name: {product_name} not found</h1>")

def filter_products(request):
    max_price = request.GET.get('max_price')