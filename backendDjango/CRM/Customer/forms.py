from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Customer

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'