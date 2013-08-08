from django.contrib import admin

from adminsortable.admin import SortableAdmin, SortableTabularInline
from .models import RoundaboutSlide, RoundaboutGallery


class RoundaboutSlideInline(SortableTabularInline):
    fields = ('title', 'img', 'published',)
    model = RoundaboutSlide
    extra = 1


class RoundaboutGalleryAdmin(SortableAdmin):
    list_display = ('title',)
    inlines = (RoundaboutSlideInline,)
    
    
class RoundaboutSlideAdmin(SortableAdmin):
    list_display = ('title',)


admin.site.register(RoundaboutGallery, RoundaboutGalleryAdmin)
admin.site.register(RoundaboutSlide, RoundaboutSlideAdmin)