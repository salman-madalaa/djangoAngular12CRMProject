from rest_framework import serializers
from Customer.models import Customer

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'   # this also return all the fields
        # fields = ('id',
        #           'name',
        #           'type',
        #           'phone',
        #           'address',
        #           'createdDateTime',
        #           'modifiedDateTime')
