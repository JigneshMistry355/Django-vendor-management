from rest_framework import serializers
from vendorPurchaseOrder.models import PurchaseOrder

class PurchaseOrderSerializer(serializers.ModelSerializer):
    quantity = serializers.IntegerField(read_only = True)
    class Meta:
        model = PurchaseOrder
        fields = ['id','order_date','items', 'quantity', 'vendor']
        # read_only_fields = ('po_number','quality_rating', 'status', 'issue_date', 'acknowledgment_date', 'delivery_date')

class FeedbackPurchaseOrderSerializer(serializers.ModelSerializer):
    po_number = serializers.CharField(read_only = True)
    class Meta:
        model = PurchaseOrder
        fields = ['id', 'po_number', 'quality_rating', 'status']

class VendorAcknowledgmentSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only = True)
    quality_rating = serializers.CharField(read_only = True)
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        # fields = ['id', 'po_number', 'delivery_date', 'issue_date', 'acknowledgment_date']
