from django.contrib import admin
from django import forms

from adminsortable.admin import SortableAdmin
from slideshow_parallax.models import Slide, SlidesShowGallery

class SlideAdmin(SortableAdmin):
    list_display = ('title', 'gallery', 'published',)
    
class SlidesShowGalleryAdmin(admin.ModelAdmin):
    list_display = ('title',)    
    
admin.site.register(Slide, SlideAdmin)
admin.site.register(SlidesShowGallery, SlidesShowGalleryAdmin)