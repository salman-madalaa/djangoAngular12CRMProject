from rest_framework import serializers
from OrderItem.models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = '__all__'   # this also return all the fields
        # fields = ('id',
        #           'name',
        #           'type',
        #           'phone',
        #           'address',
        #           'createdDateTime',
        #           'modifiedDateTime')
