from django.db import models

# Create your models here.

from enum import Enum

class CRMObjectType(Enum):
    CUSTOMER = "CUSTOMER"
    PRODUCT = "PRODUCT"
    CUSTOMERORDER = "CUSTOMERORDER"
    ORDERITEM = "ORDERITEM"



class Customer(models.Model):
    
    CustomerType = (
        ('WHOLESALE','WHOLESALE'),
        ('RETAILER','RETAILER')
    )
    
    name = models.CharField(max_length=255,blank=False)
    type = models.CharField(max_length=65,choices=CustomerType,null=False,blank=False)
    phone = models.BigIntegerField(null=False)
    address= models.CharField(max_length=255,null=False)
    
    class Meta:
        db_table= 'Customer'  # here we give the database table name 'Customer', other wise django create appNameClassName(CustomerCustomer) create.
        ordering = [
            '-id',      # here you can add your own order 
        ]
        
    def __str__(self):
        return self.type; 
     
    def Customer(self):
        super(CRMObjectType.CUSTOMERORDER)   