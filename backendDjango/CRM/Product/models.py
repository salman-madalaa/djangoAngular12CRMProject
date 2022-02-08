from django.db import models
from Customer.models import CRMObjectType

# Create your models here.

class Product(models.Model):
    units = models.CharField(max_length=50,null=False)
    name = models.CharField(max_length=64,null=False)
    price = models.FloatField(null=False)
    
    class Meta:
        db_table= 'Product'
        ordering = [
            '-id'
        ]
    
    def CustomerOrder(self):
        super(CRMObjectType.PRODUCT)
    
    def __init__(self):
        return self.name;