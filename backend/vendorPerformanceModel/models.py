from django.db import models
from vendorProfile.models import Vendor
from vendorPurchaseOrder.models import PurchaseOrder
from django.db.models import Count, Avg, F, ExpressionWrapper, FloatField
from django.utils import timezone 

class PerformanceModel(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete = models.CASCADE)
    date = models.DateField(auto_now_add=False)
    on_time_delivery_rate = models.FloatField(default = 0.0)
    quality_rating_avg = models.FloatField(default=0.0)
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField(default=0.0)

    @classmethod
    def calculate_performance_metrics(cls):
        vendors = Vendor.objects.all()
        
        for vendor in vendors:
            total_orders = PurchaseOrder.objects.filter(vendor = vendor).count()
            orders_delivered_on_time = PurchaseOrder.objects.filter(vendor = vendor, status="Completed").count()
            fulfillment_rate = (orders_delivered_on_time/total_orders) * 100 if total_orders != 0 else 0.0
            quality_rating_avg = PurchaseOrder.objects.filter(vendor=vendor).aggregate(avg_quality=Avg('quality_rating'))['avg_quality'] or 0.0
            average_response_time = PurchaseOrder.objects.filter(vendor=vendor).aggregate(avg_response=Avg(ExpressionWrapper(F('acknowledgment_date') - F('issue_date'), output_field=FloatField())))['avg_response'] or 0.0

            hours = average_response_time/ (3600 * 10**6)
    
            performance_instance, created = PerformanceModel.objects.get_or_create(vendor = vendor, date = timezone.now().date())
            performance_instance.on_time_delivery_rate = round(fulfillment_rate, 2)
            performance_instance.quality_rating_avg = round(quality_rating_avg, 2)
            performance_instance.average_response_time = round(hours,2)
            performance_instance.fulfillment_rate = round(fulfillment_rate, 2)

            performance_instance.save()
          

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.id, self.vendor.name} - {self.date}"
      



