from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .serializers import CustomerSerializer

from .models import Customer 
# Create your views here.

def CustomerHomeView(request):
    return HttpResponse("This is Customer Home Page")

@csrf_exempt
def CreateCustomer(request):
    if request.method == 'POST':
        # print(JSONParser().parse(request))  # just print the data on console
        customer_data=JSONParser().parse(request)
        customer_serializer = CustomerSerializer(data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)

@api_view(['GET'])
def GetAllCustomers(request):
    ss = Customer.objects.all()
    customers = CustomerSerializer(ss, many=True)
    context= {'customers': customers.data}
    return JsonResponse(context)

@csrf_exempt
def UpdateCustomer(request,id):
    if request.method == 'POST':     
        customer_data=JSONParser().parse(request)
        customer = Customer.objects.get(id=int(id))
        customer_serializer = CustomerSerializer(customer,data=customer_data)
        if customer_serializer.is_valid():
            customer_serializer.save()
            context= {'customer': customer_serializer.data}
            return JsonResponse(context)
        return JsonResponse("Failed to Updated.",safe=False)

    # ---------------anothe way WithOut using serializers ---------------
    # ------not that much prefer because if we have edit more fields it will be difficult---
    # if request.method == 'POST':   
    #     customer_data=JSONParser().parse(request)
    #     customer = Customer.objects.get(id=int(id))
    #     customer.name = customer_data['name']
    #     customer.type = customer_data['type']
    #     customer.phone = customer_data['phone']
    #     customer.address = customer_data['address']
    #     customer.save();
    #     return JsonResponse('customer updated successfully', safe=False);
    # else:
    #     return JsonResponse('updation failure', safe=False);

@csrf_exempt
def DeleteCustomer(request,id):
    customer = Customer.objects.get(id =int(id))
    customer.delete()
    return JsonResponse('customer deleted successfully',safe=False)