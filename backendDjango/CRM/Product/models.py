from django.db import models
from Customer.models import CRMObjectType

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=64,null=False)
    price = models.FloatField(null=False)
    units = models.IntegerField(null=False)
    
    class Meta:
        db_table= 'Product'
        ordering = [
            '-id'
        ]
    
    def __str__(self):
        return self.name

    def Product(self):
        super(CRMObjectType.PRODUCT)
    
    