from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def OrderItemHomeView(request):
    return HttpResponse("This is OrderItem Home Page")