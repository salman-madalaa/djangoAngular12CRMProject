from rest_framework import serializers
from Product.models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'   # this also return all the fields
        # fields = ('id',
        #           'name',
        #           'type',
        #           'phone',
        #           'address',
        #           'createdDateTime',
        #           'modifiedDateTime')
