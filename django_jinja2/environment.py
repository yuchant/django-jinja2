"""
Jinja 2 Environment Setup
=========================


By Yuji Tomita
12/07/2011
"""
from django.template import loader

from . import jinja2_settings

import jinja2

class Settings(object):
    FOO = 'bar'
settings = Settings()


def setup_jinja_environment():
    """
    Load jinja environment based on active django template loaders or 
    settings.JINJA2_TEMPLATE_LOADERS override.

    Populate jinja global context with settings.JINJA2_GLOBAL_CONTEXT
    """
    template_dirs = []

    for loader_string in jinja2_settings.JINJA2_TEMPLATE_LOADERS:
        [template_dirs.append(x) for x in loader.find_template_loader(loader_string).get_template_sources('')]


    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_dirs),
        extensions=jinja2_settings.JINJA2_EXTENSIONS,
        undefined=jinja2_settings.JINJA2_UNDEFINED_CLASS,
        # **jinja2_settings.JINJA2_ENVIRONMENT_KWARGS,
        )
    env.template_class = jinja2_settings.Jinja2DjangoTemplate

    jinja_context = jinja2_settings.JINJA2_GLOBAL_CONTEXT

    try:
        for key, value in jinja_context.items():
            env.globals[key] = value
    except (ValueError, AttributeError), e:
        raise Exception("Trouble applying setting 'JINJA2_GLOBALS': {0}".format(e))

    return env


jinja_env = setup_jinja_environment()
