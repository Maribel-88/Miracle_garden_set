import uuid

from django.db import models
from gardensets.models import Gardenset



class Lists_refund(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    email = models.EmailField(max_length=254, null=False, blank=False, default='')
    full_name = models.CharField(max_length=50, null=False, blank=False, default='')                              
    canceled_order = models.BooleanField(default=False)
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

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.refund_number:
            self.refund_number = self._generate_refund_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number    

    def order_date(self):
        return self.date