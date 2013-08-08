from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from models import SlidesShowGalleryPlugin  

class SlidesShowPlugin(CMSPluginBase):
    model = SlidesShowGalleryPlugin
    name = _("Slideshow Parallax")
    render_template = "slideshow_parallax/cmsplugin_slideshow_parallax.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['slides'] = instance.gallery.slide_set.filter(published=True)
        return context

plugin_pool.register_plugin(SlidesShowPlugin)