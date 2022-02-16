from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from rest_framework.decorators import api_view
from .serializers import CustomerOrderSerializer,CreatedCustomerOrderSerializer

from .models import CustomerOrder
from Customer.models import Customer
from Customer.serializers import CustomerSerializer
# Create your views here.

def CustomerOrderHomeView(request):
    return HttpResponse("This is CustomerOrder Home Page")

@csrf_exempt
def CreateCustomerOrder(request):
    if request.method == 'POST':
        # print(JSONParser().parse(request))  # just print the data on console
        CustomerOrder_data=JSONParser().parse(request)
        CustomerOrder_serializer = CreatedCustomerOrderSerializer(data=CustomerOrder_data)
        if CustomerOrder_serializer.is_valid():
            CustomerOrder_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)

@api_view(['GET'])
def GetAllCustomerOrders(request):
    customers = Customer.objects.all();
    customersOrders = CustomerOrder.objects.all();
    CustomerSerializers = CustomerSerializer(customers, many=True)
    CustomerOrderSerializer1 = CustomerOrderSerializer(customersOrders, many=True)
    context= {'CustomerOrders': CustomerOrderSerializer1.data,'customers': CustomerSerializers.data}
    return JsonResponse(context)

@csrf_exempt
def UpdateCustomerOrder(request,id):
    if request.method == 'POST':     
        newCustomerOrder_data = JSONParser().parse(request)
        oldCustomerOrder = CustomerOrder.objects.get(id =int(id))
        customerOrder_serializer = CreatedCustomerOrderSerializer(oldCustomerOrder,data=newCustomerOrder_data)
        if customerOrder_serializer.is_valid():
            customerOrder_serializer.save()
            context= {'CustomerOrder': customerOrder_serializer.data}
            return JsonResponse(context)
        return JsonResponse("Failed to Updated.",safe=False)

  
@csrf_exempt
def DeleteCustomerOrder(request,id):
    customerOrder = CustomerOrder.objects.get(id =int(id))
    customerOrder.delete()
    return JsonResponse('CustomerOrder deleted successfully',safe=False)
    