Default Settings
----------------

The default settings can be overriden via your django site settings.


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