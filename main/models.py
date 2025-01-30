from django.db import models

class Artwork(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='artworks/')  # تصاویر در media/artworks ذخیره می‌شوند.
    description = models.TextField(blank=True)  # فیلد توضیحات
    purchase_link = models.URLField(blank=True)  # فیلد لینک خرید

    def __str__(self):
        return self.title  # این متد در ادمین پنل عنوان اثر را نمایش می‌دهد.

