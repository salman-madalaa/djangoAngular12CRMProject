from django.urls import path
from . import views
urlpatterns = [
    path('', views.OrderItemHomeView, name = 'OrderItemHomeView'),
]
