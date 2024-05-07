from vendorProfile.models import Vendor
from vendorProfile.serializers import VendorSerializer
from rest_framework import generics


class CreateVendor(generics.CreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class ListVendor(generics.ListAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    def get_queryset(self):
        Vendor.calculate()
        return  super().get_queryset()


class GetVendor(generics.RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class UpdateVendor(generics.RetrieveUpdateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


class DeleteVendor(generics.DestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

