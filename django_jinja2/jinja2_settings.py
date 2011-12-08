"""
Default settings for django jinja2
==================================

Settings are in setup_defaults() function to be a bit more DRY about
defining variables and their string representations.

By Yuji Tomita
12/08/2011
"""
import os

from django.conf import settings
from django.core.urlresolvers import reverse

import jinja2


class Jinja2DjangoTemplate(jinja2.Template):
    def render(self, context):
        # flatten the Django Context into a single dictionary.
        context_dict = {}
        for d in context.dicts:
            context_dict.update(d)
        return super(Jinja2DjangoTemplate, self).render(context_dict)


class Jinja2UndefinedClass(jinja2.Undefined):
    # http://jinja.pocoo.org/docs/api/#jinja2.Undefined
    # __iter__ = Undefined._fail_with_undefined_error # force certain methods to fail
    
    def __init__(self, *args, **kwargs):
        print args, kwargs
    

    def __str__(self):
        return ''

    def __unicode__(self):
        return ''
    
    def __getattr__(self, val):
        return self.self

    def __getitem__(self):
        return self.self

    def self(_self):
        return _self



def setup_defaults():
    # global jinja context populated with the following
    JINJA2_GLOBAL_CONTEXT = {
        'reverse': reverse,
        'MEDIA_URL': settings.MEDIA_URL,
        'STATIC_URL': getattr(settings, 'STATIC_URL', ''),
    }

    JINJA2_EXTENSIONS = []

    # can be a function which accepts a template name / template dirs
    # one could potentially read the file and ensure there's a flag or certain pattern at the start of file, etc.
    JINJA2_ENGINE_CONDITION = lambda template_path: 'jinja' in os.path.basename(template_path).split('.')

    # the files accessible to these django template loaders are pulled into the jinja environment
    JINJA2_TEMPLATE_LOADERS = settings.TEMPLATE_LOADERS

    # override the jinja 2 template class as required
    JINJA2_TEMPLATE_CLASS = Jinja2DjangoTemplate

    if settings.DEBUG:
        JINJA2_UNDEFINED_CLASS = Jinja2UndefinedClass

    else:
        JINJA2_UNDEFINED_CLASS = Jinja2UndefinedClass


    for key, value in locals().items():
        globals()[key] = getattr(settings, key, value)


setup_defaults()
