from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
import jsonfield

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length = 10,unique=True)
    contact_details = models.TextField(max_length = 180)
    address = models.TextField(max_length = 180)
    vendor_code = models.CharField(max_length = 15)
    on_time_delivery_rate=models.FloatField(default=0)
    quality_rating_avg=models.FloatField(default=0)
    average_response_time=models.FloatField(default=0)
    fulfillment_rate=models.FloatField(default=0)

    def __str__(self):
        return self.name
    
class PurchaseOrder(models.Model):
    po_number=models.CharField(max_length=15)
    vendor=models.ForeignKey(Vendor,on_delete = models.CASCADE, blank = True, null = True)
    order_date=models.DateTimeField()
    delivery_date=models.DateTimeField(null=True,blank=True)
    items=jsonfield.JSONField()
    quantity=models.IntegerField()
    status=models.CharField(max_length=10)
    quality_rating=models.FloatField(null=True,blank=True)
    issue_date=models.DateTimeField()
    acknowledgement_date=models.DateTimeField(null=True,blank=True)


    def __str__(self):
        return self.po_number
    

class HistoricalPerformance(models.Model):
    vendor=models.ForeignKey(Vendor,on_delete = models.CASCADE, blank = True, null = True)
    date=models.DateTimeField(auto_now_add=True)
    on_time_delivery_rate=models.FloatField(default=0)
    quality_rating_avg=models.FloatField(default=0)
    average_response_time=models.FloatField(default=0)
    fulfillment_rate=models.FloatField(default=0)

    def __str__(self):
        return self.vendor.name