from django.contrib import admin
from .models import Eyewear, EyewearDetails, cart,CustomerDetails
from django.utils.html import format_html

# Register your models here.
class EyewearAdmin(admin.ModelAdmin):
    list_display = ['productId', 'productName', 'productPrice', 'productDescription', 'stockQuantity']
admin.site.register(Eyewear, EyewearAdmin)

class EyewearDetailsAdmin(admin.ModelAdmin):
    list_display = ['eyewear', 'brand', 'material', 'frameType']
admin.site.register(EyewearDetails, EyewearDetailsAdmin)


from .models import LensProduct

class LensProductAdmin(admin.ModelAdmin):
    list_display = ['BrandName','productName', 'productDesc', 'productPrice', 'productImage', 'productRating', 'productCategory','is_deleted','delete_details','productImage_main','productImage_side','productImage_back','productImage_top']
admin.site.register(LensProduct, LensProductAdmin)

class cartAdmin(admin.ModelAdmin):
    list_display = ['uid','pid', 'qty']
admin.site.register(cart,cartAdmin)

class CustomerDetailsAdmin(admin.ModelAdmin):
    list_display=['custname','custEmail','custAddress','custcontact','pincode']
admin.site.register(CustomerDetails,CustomerDetailsAdmin)


from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0  # Prevents showing empty extra fields

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'user', 'total_amount', 'payment_status', 'order_status', 'created_at')
    list_filter = ('payment_status', 'order_status', 'created_at')
    search_fields = ('order_id', 'user__username', 'user__email')
    ordering = ('-created_at',)
    inlines = [OrderItemInline]  # Displays order items inline

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)






