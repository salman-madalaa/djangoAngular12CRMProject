from django.urls import path
from . import views
urlpatterns = [
    path('', views.CustomerHomeView, name = 'CustomerHomeView'),
    path('new/', views.CreateCustomer, name = 'CreateCustomer'),
    path('getAll/', views.GetAllCustomers, name = 'GetAllCustomers'),
    path('update/<str:id>', views.UpdateCustomer, name = 'UpdateCustomer'),
    path('delete/<str:id>', views.DeleteCustomer, name = 'DeleteCustomer'),
]
