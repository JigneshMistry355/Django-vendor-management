from vendorPurchaseOrder.models import PurchaseOrder
from vendorPurchaseOrder.serializers import PurchaseOrderSerializer, FeedbackPurchaseOrderSerializer, VendorAcknowledgmentSerializer
from rest_framework import generics
from vendorPerformanceModel.models import PerformanceModel
from vendorProfile.models import Vendor


''' ------ Get Orders from the Client / Customer ------- '''

class CreatePurchaseOrder(generics.CreateAPIView):
    serializer_class = PurchaseOrderSerializer
    def perform_create(self, serializer):
        instance = serializer.save()
        PerformanceModel.calculate_performance_metrics()
        Vendor.calculate()


''' ------ Acknowledge the Orders from the client ------ '''

class UpdateVendorAcknowledgment(generics.RetrieveUpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = VendorAcknowledgmentSerializer
    def perform_update(self, serializer):
        instance = serializer.save()
        PerformanceModel.calculate_performance_metrics()
        Vendor.calculate()


''' ------ At delivery, take feedback from client --------'''

class UpdatePurchaseOrderFeedback(generics.RetrieveUpdateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = FeedbackPurchaseOrderSerializer
    def perform_update(self, serializer):
        instance = serializer.save()
        PerformanceModel.calculate_performance_metrics()
        Vendor.calculate()
    

''' --------- List all the orders in the system -------- '''

class ListPurchaseOrder(generics.ListAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

    def get_queryset(self):
        PerformanceModel.calculate_performance_metrics()
        Vendor.calculate()
        return super().get_queryset()


''' ---------- Get single order record using id -------'''

class GetPurchaseOrder(generics.RetrieveAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


''' ----------------- Delete a record -------------------'''

class DeletePurchaseOrder(generics.DestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    def perform_destroy(self, instance):
        instance.delete()
        PerformanceModel.calculate_performance_metrics()
        Vendor.calculate()
