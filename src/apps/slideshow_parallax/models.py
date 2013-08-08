from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from adminsortable.models import Sortable


class SlidesShowGallery(models.Model):
    title = models.CharField(_('Title'), max_length=128)
    
    class Meta():
        verbose_name = _('Slide gallery')
        verbose_name_plural = _('Slides galleries')
    
    def __unicode__(self):
        return self.title


class Slide(Sortable):
    title = models.CharField(_('Title'), max_length=128, 
            help_text=("&lt;span&gt; niebieski tekst &lt;/span&gt;") )
    
    gallery = models.ForeignKey(SlidesShowGallery, blank=True, null=True)
    description = models.TextField(_('Description'), max_length=255, blank=True, null=True)
    btn_text = models.CharField(_('Button text'), max_length=40, blank=True, null=True  )
    url = models.CharField(_('link url'), max_length=255, blank=True, null=True)
    img = models.ImageField(_('Image'), upload_to='slideshow-paralax')
    published = models.BooleanField(_('Published'), default=True)
    
    class Meta(Sortable.Meta):
        verbose_name = _('Slide')
        verbose_name_plural = _('Slides')
        
    def __unicode__(self):
        return self.title
    
class SlidesShowGalleryPlugin(CMSPlugin):
    gallery = models.ForeignKey(SlidesShowGallery)