from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')

def contact(request):
    return render(request, 'main/contact.html')

def products(request):
    return render(request, 'main/products.html')

def artworks(request):
    return render(request, 'main/artworks.html')

def articles(request):
    return render(request, 'main/articles.html')