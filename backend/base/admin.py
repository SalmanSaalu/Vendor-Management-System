from django.contrib import admin
from .models import Vendor,PurchaseOrder,HistoricalPerformance
# Register your models here.
admin.site.register(Vendor)

class purchase_order_Admin(admin.ModelAdmin):
    list_display = ['po_number','vendor','status','issue_date','acknowledgement_date','delivery_date']
admin.site.register(PurchaseOrder, purchase_order_Admin)

class historical_performance_Admin(admin.ModelAdmin):
    list_display = ['vendor']
admin.site.register(HistoricalPerformance, historical_performance_Admin)