from django.contrib import admin
from vendorProfile.models import Vendor

class VendorAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'vendor_code', 'on_time_delivery_rate','quality_rating_avg','average_response_time', 'fulfillment_rate')

# Register your models here.
admin.site.register(Vendor, VendorAdmin)

# username : VendorAdmin
# email : vendoradmin@gmail.com
#password : 123
