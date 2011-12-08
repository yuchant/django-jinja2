from django.template.loaders.app_directories import Loader

from .base import ConditionalJinja2LoaderMixin


class Loader(ConditionalJinja2LoaderMixin, Loader):
    pass

_loader = Loader()