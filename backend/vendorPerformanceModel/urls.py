from django.urls import path
from vendorPerformanceModel.views import GetVendorPerformance, CreateVendorPerformance, UpdatePerformanceModel


urlpatterns = [
    path('get-vendor-performance/', GetVendorPerformance.as_view(), name = "Vendor Performance"),
    path('post-vendor-performance/', CreateVendorPerformance.as_view(), name = "Generate Performance"),
    path('update-vendor-performance/<int:pk>/', UpdatePerformanceModel.as_view(), name="Update Performane"),
]