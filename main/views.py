from django.shortcuts import render
from .models import Artwork  # اضافه کردن مدل Artwork

def home(request):
    artworks = Artwork.objects.all()[:8]  # نمایش ۸ اثر اول
    return render(request, 'main/home.html', {'artworks': artworks})  # ارسال داده‌ها به قالب

def contact(request):
    return render(request, 'main/contact.html')

def products(request):
    return render(request, 'main/products.html')

def artworks(request):
    artworks = Artwork.objects.all()[:8]  # نمایش ۸ اثر اول
    return render(request, 'main/artworks.html', {'artworks': artworks})  # ارسال داده‌ها به قالب

def articles(request):
    return render(request, 'main/articles.html')