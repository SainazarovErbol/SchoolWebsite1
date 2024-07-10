from django.contrib import admin
from .models import Gallery, Image, Video

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')
    search_fields = ('title', 'description')


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('gallery', 'caption')
    list_filter = ('gallery',)


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('gallery', 'caption')
    list_filter = ('gallery',)
