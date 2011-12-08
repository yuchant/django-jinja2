from django.template.loaders.filesystem import Loader

from .base import ConditionalJinja2LoaderMixin


class Loader(ConditionalJinja2LoaderMixin, Loader):
    pass

_loader = Loader()