from django.urls import path
from vendorPurchaseOrder.views import CreatePurchaseOrder, ListPurchaseOrder, GetPurchaseOrder, UpdatePurchaseOrderFeedback, UpdateVendorAcknowledgment, DeletePurchaseOrder

urlpatterns = [
    path('post-purchase-orders/', CreatePurchaseOrder.as_view(), name = "Place Order"),
    path('get-purchase-orders/', ListPurchaseOrder.as_view(), name = "List-Purchase_Order"),
    path('retrieve-purchase-order/<int:pk>/', GetPurchaseOrder.as_view(), name = "Get-Purchase_Order"),
    path('update-purchase-order-feedback/<int:pk>/', UpdatePurchaseOrderFeedback.as_view(), name = "Customer/Client Feedback"),
    path('update-purchase-order-ack/<int:pk>/', UpdateVendorAcknowledgment.as_view(), name = "Vendor Acknowledment"),    
    path('delete-purchase-order/<int:pk>/', DeletePurchaseOrder.as_view(), name = "Delete-Purchase_Order"),
    
]