from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def ProductHomeView(request):
    return HttpResponse("This is Product Home Page")