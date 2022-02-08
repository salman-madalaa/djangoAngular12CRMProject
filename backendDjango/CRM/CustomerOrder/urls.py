from django.urls import path
from . import views
urlpatterns = [
    path('', views.CustomerOrderHomeView, name = 'CustomerOrderHomeView'),
]
