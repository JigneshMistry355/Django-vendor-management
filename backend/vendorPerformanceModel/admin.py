from django.contrib import admin
from vendorPerformanceModel.models import PerformanceModel


class PerformanceModelAdmin(admin.ModelAdmin):
    list_display = ['vendor', 'date', 'on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']


admin.site.register(PerformanceModel, PerformanceModelAdmin)