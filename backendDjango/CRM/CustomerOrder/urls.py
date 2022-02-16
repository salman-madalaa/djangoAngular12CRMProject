from django.urls import path
from . import views
urlpatterns = [
    path('', views.CustomerOrderHomeView, name = 'CustomerOrderHomeView'),
    path('new/', views.CreateCustomerOrder, name = 'CreateCustomerOrder'),
    path('getAll/', views.GetAllCustomerOrders, name = 'GetAllCustomerOrders'),
    path('update/<str:id>', views.UpdateCustomerOrder, name = 'UpdateCustomerOrder'),
    path('delete/<str:id>', views.DeleteCustomerOrder, name = 'DeleteCustomerOrder'),
]
