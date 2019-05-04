from django.contrib import admin
from shop import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    pass
