from django.db import models
from django.utils.translation import gettext as _


class Category(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=_('Название'),
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = _('Категория')
        verbose_name_plural = _('Категории')

    def __str__(self):
        return self.title


class Item(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name=_('Название'),
        null=False,
        blank=False
    )
    category = models.ForeignKey(
        to='Category',
        related_name='items',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    description = models.TextField(
        verbose_name=_('Описание'),
        null=False,
        blank=False
    )
    price = models.FloatField(
        verbose_name=_('Цена'),
        null=False,
        blank=False
    )

    class Meta:
        verbose_name = _('Товар')
        verbose_name_plural = _('Товары')

    def __str__(self):
        return f'{self.title} ({self.category.title})'