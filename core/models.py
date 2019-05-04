from django.db import models
from django.utils.translation import gettext as _


class Base(models.Model):
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('Время создания'),
        blank=True
    )
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name=_('Время обновления'),
        blank=True
    )

    class Meta:
        abstract = True
