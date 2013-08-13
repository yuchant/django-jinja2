
Introduction
============

This is an easy drop in solution for conditionally and seamlessly rendering jinja2 templates (with their context) while defaulting to the django template engine.

By default, if a filename contains a ``.jinja`` (or ``foo.jinja.html``) extension, the template will be rendered via jinja2. 

The condition can be customized via your settings.py in ``JINJA2_ENGINE_CONDITION``, a function which receives the full path to the template as the first argument. Jinja2 is used if the function returns ``True``.

> For example, you could use the engine if the file is in a directory named jinja, or read the first line of the file.

You could force all templates to use jinja2 by always returning ``True`` e.g. ``lambda x: True``

The jinja2 environment is created with the same environment the django loaders use - that is all of the directories returned by each loader defined in ``settings.TEMPLATE_LOADERS``





Installation
============


Grab code
---------

Clone the repository and and add ``django_jinja2`` to your python site packages or install using ``pip install django-jinja2``.


Add to settings.py
------------------

### Add ``'django_jinja2'`` to your installed apps

    INSTALLED_APPS = [
        # ...,
        'django_jinja2',
    ]
### Replace your template loaders with the loaders in ``django_jinja2.loaders``.

    TEMPLATE_LOADERS = (
        'django_jinja2.loaders.filesystem.Loader',
        'django_jinja2.loaders.app_directories.Loader',
    )


Done! Now all you have to do is render a template with the name ``jinja`` in the extension.



Default Settings
================

The default settings can be overridden via your django site settings.


    JINJA2_GLOBAL_CONTEXT = {
        'reverse': reverse,
        'MEDIA_URL': settings.MEDIA_URL,
        'STATIC_URL': getattr(settings, 'STATIC_URL', ''),
    }

    JINJA2_EXTENSIONS = []
    JINJA2_ENVIRONMENT_KWARGS = {}
    # kwargs passed to Jinja.Environment function (filters={})

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
