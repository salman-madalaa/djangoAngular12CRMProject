from django.shortcuts import render
from django.http.response import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CustomerSerializer


from .models import Customer 
# Create your views here.

def CustomerHomeView(request):
    return HttpResponse("This is Customer Home Page")

@csrf_exempt
def CreateCustomer(request):
    if request.method == 'POST':
        print(" data is :",request.POST)
    print("madala");
    print(request.POST.get('Customer.name'));
    print("salman");
    customer = request
    # Customer.objects.create(
    #     name = request.POST.get('customer.name'),
    #     type = request.POST.get('type'),
    #     phone = request.POST.get('phone'),
    #     address= request.POST.get('address')
    # )
    context = {'customer': customer}
    return HttpResponse("context")

@api_view(['GET'])
def GetAllCustomers(request):
    ss = Customer.objects.all()
    customers = CustomerSerializer(ss, many=True)
    context= {'customers': customers.data}
    return JsonResponse(context)

def UpdateCustomer(request,id):
    customer1 = request.POST.get('customer')
    customer = Customer.objects.get(id=int(id))
    customer.name(customer1.name)
    customer.phone(customer1.phone)
    customer.save()
    context= {'customer': customer}
    return render(request,'customer updated successfully',context)

def DeleteCustomer(request,id):
    Customer.objects.delete(id =int(id))
    return HttpResponse('customer deleted successfully')