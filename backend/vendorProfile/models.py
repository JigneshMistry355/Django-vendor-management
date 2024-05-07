from django.db import models
import uuid
from django.db.models import Avg, F, ExpressionWrapper, FloatField


class Vendor(models.Model):
    name = models.CharField(max_length=50)
    contact_details = models.TextField(max_length=200)
    address = models.TextField(max_length=200)
    vendor_code = models.CharField(blank=True,max_length=50,unique=True)
    on_time_delivery_rate = models.FloatField(default = 0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)


    @classmethod
    def calculate(cls):
        from vendorPurchaseOrder.models import PurchaseOrder
        vendors = Vendor.objects.all()
        for vendor in vendors:
            total_orders = PurchaseOrder.objects.filter(vendor=vendor).count()
            order_delivered_on_time = PurchaseOrder.objects.filter(vendor=vendor, status='Completed').count()
            fulfillment_rate = (order_delivered_on_time/total_orders) * 100 if total_orders != 0 else 0.0
            quality_rating_avg = PurchaseOrder.objects.filter(vendor=vendor).aggregate(avg_quality=Avg('quality_rating'))['avg_quality'] or 0.0
            average_response_time = PurchaseOrder.objects.filter(vendor=vendor).aggregate(avg_response=Avg(ExpressionWrapper(F('acknowledgment_date') - F('issue_date'), output_field=FloatField())))['avg_response'] or 0.0
    
            hours = average_response_time/ (3600 * 10**6)
            
            # vendor_instance, created = Vendor.objects.get_or_create(vendor = vendor)
            vendor.on_time_delivery_rate = round(fulfillment_rate, 2)
            vendor.quality_rating_avg = round(quality_rating_avg, 2)
            vendor.average_response_time = round(hours, 2)
            vendor.fulfillment_rate = round(fulfillment_rate, 2)

            vendor.save()

    def updateStats(self):
        from vendorPerformanceModel.models import PerformanceModel
        PerformanceModel.calculate_performance_metrics()

    def generate_vendor_code(self):
        random_part = str(uuid.uuid4())[:8]
        self.vendor_code = f"{self.name[:3].upper()}-{random_part}"
        self.updateStats()

    def save(self, *args, **kwargs):       
        if not self.vendor_code:
            self.generate_vendor_code()
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    



