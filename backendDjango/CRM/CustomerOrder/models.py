from django.db import models
from Customer.models import CRMObjectType

# Create your models here.

class CustomerOrder(models.Model):
    customerId = models.IntegerField(null=False, blank=False)
    orderDate = models.DateField(null=False,auto_now=True)
    contact_phone = models.BigIntegerField(null=False)
    orderTotal = models.FloatField(null=False)
    created = models.DateTimeField(null=False,auto_now_add=True)
    updated = models.DateTimeField(null=False,auto_now=True)
    
    class Meta:
        db_table = 'CustomerOrder' 
        ordering = [
            
        ]
    
    def CustomerOrder(self):
        super(CRMObjectType.CUSTOMERORDER)
    
    def __init__(self):
        return self.customerId;