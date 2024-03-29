from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Order, Customer

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer',]
        # ['customer', 'product', 'status', 'qty']


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']