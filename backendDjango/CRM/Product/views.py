from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from .serializers import ProductSerializer

from django.core.paginator import Paginator

from .models import Product 
# Create your views here.

def ProductHomeView(request):
    return HttpResponse("This is Product Home Page")

@csrf_exempt
def CreateProduct(request):
    if request.method == 'POST':
        product_data=JSONParser().parse(request)
        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)

@api_view(['GET'])
def GetAllProducts(request):
    ss = Product.objects.all()
    products = ProductSerializer(ss, many=True)
    context= {'products': products.data}
    return JsonResponse(context)

@csrf_exempt
def UpdateProduct(request,id):
    if request.method == 'POST':     
        product_data=JSONParser().parse(request)
        product = Product.objects.get(id=int(id))
        product_serializer = ProductSerializer(product,data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            context= {'product': product_serializer.data}
            return JsonResponse(context)
        return JsonResponse("Failed to Updated.",safe=False)

@csrf_exempt
def DeleteProduct(request,id):
    product = Product.objects.get(id =int(id))
    product.delete()
    return JsonResponse('product deleted successfully',safe=False)


@csrf_exempt
def GetByPageProduct(request):
    req = JSONParser().parse(request)
    count = Product.objects.all().count() # this is for total objects 
    
    allProducts = Product.objects.all()
    p = Paginator(allProducts, req['pageSize'])
    
    productss = p.page(int(req['pageIndex']) + 1)
  
    products = ProductSerializer(productss, many=True)
    
    context= {'products': products.data,'totalCount': count}
    return JsonResponse(context)

   