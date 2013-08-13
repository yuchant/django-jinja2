"""
Jinja 2 Environment Setup
=========================


By Yuji Tomita
12/07/2011
"""
from django.template import loader

from . import jinja2_settings

import jinja2


def setup_jinja_environment():
    """
    Load jinja environment based on active django template loaders or
    settings.JINJA2_TEMPLATE_LOADERS override.

    Populate jinja global context with settings.JINJA2_GLOBAL_CONTEXT
    """
    template_dirs = []

    for loader_string in jinja2_settings.JINJA2_TEMPLATE_LOADERS:
        [template_dirs.append(x) for x in loader.find_template_loader(loader_string).get_template_sources('')]

    kwargs = jinja2_settings.JINJA2_ENVIRONMENT_KWARGS.copy()
    kwargs.update({
        'loader': jinja2.FileSystemLoader(template_dirs),
        'extensions': jinja2_settings.JINJA2_EXTENSIONS,
    })

    env = jinja2.Environment(**kwargs)
    env.template_class = jinja2_settings.Jinja2DjangoTemplate

    try:
        for key, value in jinja2_settings.JINJA2_GLOBAL_CONTEXT.items():
            env.globals[key] = value
    except (ValueError, AttributeError), e:
        raise Exception("Trouble applying setting 'JINJA2_GLOBALS': {0}".format(e))

    for key, value in jinja2_settings.JINJA2_ENVIRONMENT_ATTRS.items():
        setattr(env, key, value)

    return env

jinja_env = setup_jinja_environment()
