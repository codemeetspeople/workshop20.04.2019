from django.apps import AppConfig
from django.utils.translation import gettext as _


class ShopConfig(AppConfig):
    name = 'shop'
    verbose_name = _('Магазин')
