from rest_framework import generics
from vendorPerformanceModel.serializers import PerformanceModelSerializer
from vendorPerformanceModel.models import PerformanceModel


class GetVendorPerformance(generics.ListAPIView):
    serializer_class = PerformanceModelSerializer
    def get_queryset(self):
        PerformanceModel.calculate_performance_metrics()
        queryset =  PerformanceModel.objects.all()
        return queryset   
    

class CreateVendorPerformance(generics.CreateAPIView):
    queryset = PerformanceModel.objects.all()
    serializer_class = PerformanceModelSerializer


class UpdatePerformanceModel(generics.RetrieveUpdateAPIView):
    queryset = PerformanceModel.objects.all()   
    serializer_class = PerformanceModelSerializer
