from django.db import models
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from adminsortable.models import Sortable
from adminsortable.fields import SortableForeignKey

    
class RoundaboutGallery(CMSPlugin, Sortable):
    title = models.CharField(max_length=255)
    use_fancybox = models.BooleanField(default=False)
    
    class Meta(Sortable.Meta):
        verbose_name = _('Roundabout Gallery')
        verbose_name_plural = _('Roundabout Galleries')
    
    def __unicode__(self):
        return self.title
    
    def copy_relations(self, oldinstance):
        for slide in oldinstance.slides.all():
            # instance.pk = None; instance.pk.save() is the slightly odd but
            # standard Django way of copying a saved model instance
            slide.pk = None
            slide.gallery = self
            slide.save()
    
    
class RoundaboutSlide(Sortable):
    gallery = SortableForeignKey(RoundaboutGallery, related_name='slides',
                                 verbose_name=_('Gallery'))
    title = models.CharField(_('Title'), max_length=128)
    description = models.TextField(_('Description'), max_length=255, blank=True,
                                   null=True)
    url = models.CharField(_('Link url'), max_length=255, blank=True, null=True)
    img = models.ImageField(_('Image'), upload_to='slideshow-roundabout')
    published = models.BooleanField(_('Published'), default=True)
    
    class Meta(Sortable.Meta):
        verbose_name = _('Roundabout Slide')
        verbose_name_plural = _('Roundabout Slides')
        
    def __unicode__(self):
        return self.title
