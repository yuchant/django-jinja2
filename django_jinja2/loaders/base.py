"""
Jinja Template Loader Mixin
============

Plug into default django template loaders and use Jinja if file matches pattern
in settings.JINJA2_ENGINE_CONDITION

By Yuji Tomita
12/07/2011
"""
from django.template.base import TemplateDoesNotExist

import jinja2

from .. import jinja2_settings


class ConditionalJinja2LoaderMixin(object):
    """
    Used for overriding django's default template loaders
    with jinja if a certain condition is met.
    """
    def load_template(self, template_name, template_dirs=None):
        from ..environment import jinja_env
        condition = jinja2_settings.JINJA2_ENGINE_CONDITION

        if condition(template_name) == True:
            try:
                template = jinja_env.get_template(template_name)
            except jinja2.TemplateNotFound:
                raise TemplateDoesNotExist(template_name)
            return template, template.filename

        return super(ConditionalJinja2LoaderMixin, self).load_template(template_name, template_dirs)
        
