from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),  # مسیر جدید برای صفحه راه‌های ارتباطی
]

if settings.DEBUG:  # اضافه کردن مسیر MEDIA فقط در حالت Debug
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)