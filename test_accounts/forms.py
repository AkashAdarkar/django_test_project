from django.forms import ModelForm
# from django.forms import inlineformset_factory

from .models import Order,Customer

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'



class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name','phone','email']

# OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=1)