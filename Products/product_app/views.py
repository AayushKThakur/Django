from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,Http404

# Create your views here.

products={
    1:{'name' : 'A', 'price' : 1500},
    2:{'name' : 'B', 'price' : 1100},
    3:{'name' : 'C', 'price' : 150},
}

def home(request):
    return HttpResponse("<h1>Welcome to Product Store</h1>")

def all_products(request):
    product_items={product['name']: product['price'] for product in products.values() }
    return JsonResponse(product_items)