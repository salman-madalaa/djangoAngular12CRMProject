from django.urls import path
from . import views
urlpatterns = [
    path('', views.ProductHomeView, name = 'ProductHomeView'),
    path('new/', views.CreateProduct, name = 'CreateProduct'),
    path('getAll/', views.GetAllProducts, name = 'GetAllProducts'),
    path('update/<str:id>', views.UpdateProduct, name = 'UpdateProduct'),
    path('delete/<str:id>', views.DeleteProduct, name = 'DeleteProduct'),
    path('get/page/', views.GetByPageProduct, name = 'GetByPageProduct'),
]
