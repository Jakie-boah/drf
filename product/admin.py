from django.contrib import admin

from .models import *
from django.urls import reverse
from django.utils.safestring import mark_safe


class EditLinkInLine:
    def edit(self, instance):
        url = reverse(
            f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change",
            args=(instance.pk,),
        )
        if instance.pk:
            return mark_safe('<a href="{u}">edit</a>'.format(u=url))
        else:
            return ''


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductLineInline(EditLinkInLine, admin.TabularInline):
    model = ProductLine
    readonly_fields = ('edit',)


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductLineInline
    ]


class ProductLineAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


admin.site.register(ProductLine, ProductLineAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
