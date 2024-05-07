from rest_framework import serializers
from vendorPerformanceModel.models import PerformanceModel

class PerformanceModelSerializer(serializers.ModelSerializer):
    on_time_delivery_rate = serializers.FloatField(read_only = True)
    quality_rating_avg = serializers.FloatField(read_only = True)
    average_response_time = serializers.FloatField(read_only = True)
    fulfillment_rate = serializers.FloatField(read_only = True)
    class Meta:
        model = PerformanceModel
        fields = '__all__'