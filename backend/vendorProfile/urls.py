from django.urls import path
from vendorProfile.views import CreateVendor, ListVendor, GetVendor, UpdateVendor, DeleteVendor

urlpatterns = [
    path('post-vendors/', CreateVendor.as_view(), name = "Create-Vendor-Profile"),
    path('get-vendor/', ListVendor.as_view(), name = "List-Vendor-Profile"),
    path('retrieve-vendor/<int:pk>/', GetVendor.as_view(), name = "Retrieving-Vendor"),
    path('update-vendor/<int:pk>/', UpdateVendor.as_view(), name = "Update-Vendor"),
    path('delete-vendor/<int:pk>/',  DeleteVendor.as_view(), name = "Delete-Vendor"),

    
]