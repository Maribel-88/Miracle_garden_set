from django.contrib import admin
from .models import Lists_refund


class Lists_refundAdmin(admin.ModelAdmin):
    list_display = (
        'order_number',
        'full_name',
        'email',
        'order_to_be_cancelled', 
        'date',
        'refund_status',
        'refund_number',
        
    )

admin.site.register(Lists_refund,Lists_refundAdmin) 

