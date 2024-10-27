import uuid

from django.db import models
from gardensets.models import Gardenset



class Lists_refund(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    email = models.EmailField(max_length=254, null=False, blank=False, default='')
    full_name = models.CharField(max_length=50, null=False, blank=False, default='')                              
    order_to_be_cancelled = models.TextField(Gardenset, null=False, blank=False, default='')
    date = models.DateTimeField(auto_now_add=True)
    refund_status = models.BooleanField(default=False)
    refund_number = models.CharField(max_length=32, null=False, editable=False)


    def _generate_refund_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def __str__(self):
        return self.order_number

    def order_date(self):
        return self.date