from django.contrib import admin
from vendorPurchaseOrder.models import PurchaseOrder

class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('id','vendor', 'po_number', 'items', 'quantity', 'order_date','issue_date','acknowledgment_date', 'delivery_date', 'quality_rating', 'status')

admin.site.register(PurchaseOrder, PurchaseOrderAdmin)