from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .serializers import OrderItemSerializer

from .models import OrderItem 
# Create your views here.

def OrderItemHomeView(request):
    return HttpResponse("This is OrderItem Home Page")

@csrf_exempt
def CreateOrderItem(request):
    if request.method == 'POST':
        orderItem_data=JSONParser().parse(request)
        orderItem_serializer = OrderItemSerializer(data=orderItem_data)
        if orderItem_serializer.is_valid():
            orderItem_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)

@api_view(['GET'])
def GetAllOrderItems(request):
    ss = OrderItem.objects.all()
    orderItems = OrderItemSerializer(ss, many=True)
    context= {'orderItems': orderItems.data}
    return JsonResponse(context)

@csrf_exempt
def UpdateOrderItem(request,id):
    if request.method == 'POST':     
        orderItem_data=JSONParser().parse(request)
        orderItem = OrderItem.objects.get(id=int(id))
        orderItem_serializer = OrderItemSerializer(orderItem,data=orderItem_data)
        if orderItem_serializer.is_valid():
            orderItem_serializer.save()
            context= {'orderItem': orderItem_serializer.data}
            return JsonResponse(context)
        return JsonResponse("Failed to Updated.",safe=False)

@csrf_exempt
def DeleteOrderItem(request,id):
    orderItem = OrderItem.objects.get(id =int(id))
    orderItem.delete()
    return JsonResponse('orderItem deleted successfully',safe=False)