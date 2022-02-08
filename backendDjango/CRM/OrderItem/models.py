from django.db import models
from Customer.models import CRMObjectType

# Create your models here.

class OrderItem(models.Model):
    
    orderId = models.IntegerField(null=False, blank=True)
    productId = models.IntegerField(null=False)
    quality = models.TextField(null=False,max_length=100,blank=False)
    itemTotal = models.FloatField(null=False)
    
    class Meta:
        db_table= 'OrderItem'
        ordering = [
            '-id'
        ]
    
    def CustomerOrder(self):
        super(CRMObjectType.ORDERITEM)
    
    def __init__(self):
        return self.orderId;