from vendorProfile.models import Vendor
from rest_framework import serializers

class VendorSerializer(serializers.ModelSerializer):
    vendor_code = serializers.CharField(read_only = True)
    on_time_delivery_rate = serializers.FloatField(read_only = True)
    quality_rating_avg = serializers.FloatField(read_only = True)
    average_response_time = serializers.FloatField(read_only = True)
    fulfillment_rate = serializers.FloatField(read_only = True)
    class Meta:
        model = Vendor
        fields = '__all__'

