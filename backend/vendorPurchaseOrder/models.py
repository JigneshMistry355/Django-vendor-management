from django.db import models
from vendorProfile.models import Vendor
import uuid


class PurchaseOrder(models.Model):
    po_number = models.CharField(blank=True,max_length = 50)
    vendor = models.ForeignKey(Vendor, on_delete = models.CASCADE)
    order_date = models.DateTimeField(auto_now = False, auto_now_add = False)
    delivery_date = models.DateTimeField(auto_now = False, auto_now_add = False, null=True, blank=True)
    items = models.JSONField()
    quantity = models.IntegerField(default = 0, blank=True)
    status = models.CharField(max_length = 50, default="Pending")
    quality_rating = models.FloatField(default = 0.0)
    issue_date = models.DateTimeField(auto_now = False, auto_now_add = False,null=True, blank=True)
    acknowledgment_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)


    def updateStats(self):
        from vendorPerformanceModel.models import PerformanceModel
        PerformanceModel.calculate_performance_metrics()
    
    def updateVendorStats(self):
        from vendorProfile.models import Vendor
        Vendor.calculate()

    def generate_po_number(self):
        random_part = str(uuid.uuid4())[:8]
        self.po_number = f"PO - {random_part}"

    def calculate_total_quantity(self):
        total_quantity = sum(self.items.values())
        self.quantity = total_quantity
 
    def save(self, *args, **kwargs):
        self.updateVendorStats()
        self.updateStats()
        self.calculate_total_quantity()
        if not self.po_number:
            self.generate_po_number()
        super().save(*args, **kwargs)

    
    def __str__(self):
        return f"{self.vendor} {self.id}"
    
   




   # def get_on_time_delivery_rate(self):
    #     total_orders = PurchaseOrder.objects.filter(vendor=self.vendor).count()
    #     # from vendorPerformanceModel.models import PerformanceModel
    #     # per_obj = PerformanceModel()
    #     # delivery_rate = per_obj.get_on_time_delivery_rate()
    #     # return delivery_rate




#     def total_orders(self):
#         return PurchaseOrder.objects.filter(vendor=self.vendor).count()

#     def delivery_rate(self):
#         on_time = PurchaseOrder.objects.filter(vendor = self.vendor, status = 'Completed' ).count()
#         self.on_time_delivery_rate = (on_time/self.total_orders()) * 100
    
#     def save(self, *args, **kwargs):
#         self.delivery_rate()
#         super().save(*args, **kwargs)


  # def total_orders(self):
    #     return PurchaseOrder.objects.filter(vendor=self).count()
    

    # def on_time_delivered_orders(self):
    #     return PurchaseOrder.objects.filter(status='Completed').count()
    

    # def calculate_on_time_delivery_rate(self):
    #     total_orders = self.total_orders()
    #     if total_orders == 0:
    #         return 0.0
    #     else:
    #         on_time_delivered_orders = self.on_time_delivered_orders()
    #         Vendor.on_time_delivery_rate = f"{(on_time_delivered_orders/total_orders) * 100}"
            