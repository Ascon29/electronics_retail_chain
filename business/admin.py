from django.contrib import admin
from django.utils.html import format_html

from business.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "supplier_link", "hierarchy_level", "debt", "creation_time")
    list_filter = ("city",)
    actions = ["clear_debt"]

    @admin.display(description="Ссылка на поставщика")
    def supplier_link(self, obj):
        """ Добавление ссылки на поставщика """
        if obj.supplier:
            return format_html("<a href='{url}'>{url_name}</a>", url=obj.supplier.id, url_name=obj.supplier)

    @admin.action(description="Очистить задолженность перед поставщиком")
    def clear_debt(self, request, queryset):
        """ Admin action, очищающий задолженность перед поставщиком у выбранных объектов. """
        queryset.update(debt=0)
        self.message_user(request, "Задолженность перед поставщиком очищена")
