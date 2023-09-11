from django.contrib import admin

from orderCare import models


# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('customer_code', 'customer_name')
    search_fields = ('customer_code', 'customer_name')
    ordering = ('customer_code',)


class ItemAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'item_name', 'item_amount')
    search_fields = ('uuid', 'item_name')
    ordering = ('uuid',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'customer', 'amount')
    search_fields = ('uuid',)
    ordering = ('uuid',)


admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Order, OrderAdmin)
