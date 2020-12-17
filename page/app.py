from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class PageConfig(AppConfig):
    name = 'page'
    verbose_name = _('page')

    def ready(self):
        import page.signal
