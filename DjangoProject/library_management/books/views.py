from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to the Library</h1>")

def about(request):
    return HttpResponse("<h1>This Page is for About US</h1>")

def contact(request):
    return HttpResponse("<h1>This Page is for Contact US</h1>")
#view all books
def all books(request):
    return HttpResponse({'books':BOOKS})
def books_details(request):
    return HttpResponse("<h1>The details of book are: ID:{id}</h1>")
def books_details(request, book_id):
    book = ((book for book in BOOKS if book['id']==book_id))
    returb JsonResponse({'book': book} if book else {f'message':"Book ID with {book_id} not found"})

