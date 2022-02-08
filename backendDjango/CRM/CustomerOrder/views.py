from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def CustomerOrderHomeView(request):
    return HttpResponse("This is CustomerOrder Home Page")