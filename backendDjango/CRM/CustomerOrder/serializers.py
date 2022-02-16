from rest_framework import serializers
from CustomerOrder.models import CustomerOrder

class CustomerOrderSerializer(serializers.ModelSerializer):
    # orderDate = serializers.DateField(format="%d-%m-%Y")
    created = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    updated = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    
    class Meta:
        model = CustomerOrder
        fields = '__all__'   # this also return all the fields
        # fields = ('id',
        #           'name',
        #           'type',
        #           'phone',
        #           'address',
        #           'createdDateTime',
        #           'modifiedDateTime')



class CreatedCustomerOrderSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = CustomerOrder
        fields = '__all__'   # this also return all the fields
        # fields = ('id',
        #           'name',
        #           'type',
        #           'phone',
        #           'address',
        #           'createdDateTime',
        #           'modifiedDateTime')
