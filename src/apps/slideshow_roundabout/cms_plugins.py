from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from adminsortable.admin import SortableAdmin

from .models import RoundaboutGallery
from .admin import RoundaboutSlideInline


class RoundaboutPlugin(CMSPluginBase, SortableAdmin):
    model = RoundaboutGallery
    inlines = (RoundaboutSlideInline,)
    change_form_template_extends = CMSPluginBase.change_form_template
    name = _("Slideshow Roundabaout")
    render_template = "slideshow_roundabout/cmsplugin_slideshow_roundabout.html"
    
    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['slides'] = instance.slides.filter(published=True)
        return context

plugin_pool.register_plugin(RoundaboutPlugin)