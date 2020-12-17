from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class CustomerConfig(AppConfig):
    name = 'customer'
    verbose_name = _('customer')
