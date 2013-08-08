# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from cmsplugin_plaintext.models import CMSTextFieldPlugin

class TextFieldPlugin(CMSPluginBase):
    model = CMSTextFieldPlugin
    name = _('plaintext text area')
    render_template = 'cmsplugin_plaintext/text.html'

    def render(self, context, instance, placeholder):
        context.update({
            'body': instance.body,
            'object': instance,
            'placeholder': placeholder
        })
        return context

plugin_pool.register_plugin(TextFieldPlugin)
