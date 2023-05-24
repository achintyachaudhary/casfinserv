from django.contrib import admin

from core.models import BTSTStock, Stock


class BTSTAdmin(admin.ModelAdmin):
    list_display = ('stock', 'closing_price', 'percentage_change', 'next_day_opening', 'volume', 'created_at')
    list_filter = ('stock', 'closing_price', 'percentage_change', 'volume', 'next_day_opening', 'created_at')
    search_fields = ('stock', 'closing_price', 'percentage_change', 'volume', 'next_day_opening', 'created_at')


class StockAdmin(admin.ModelAdmin):
    list_display = ('name', 'nse_code', 'price')  # Customize the fields displayed in the list view
    list_filter = ('name', 'nse_code', 'price')  # Add filters to the right sidebar
    search_fields = ('name', 'nse_code', 'price')  # Enable search functionality


admin.site.register(Stock, StockAdmin)
admin.site.register(BTSTStock, BTSTAdmin)
