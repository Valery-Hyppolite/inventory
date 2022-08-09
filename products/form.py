
#from warnings import _catch_warnings_without_records
from django.forms import ModelForm, fields, widgets
from .models import *

class CategoryForm(ModelForm):
    class Meta:
        model = Catagory
        fields = '__all__'

    def __init__(self, *arg, **kwargs):
       super(OrderItemForm, self).__init__(*arg, **kwargs)



class ProductForm(ModelForm):
    class Meta:
        model   = Product
        fields  = ['category', 'name', 'price', 'quantity', 'total_cost']
    
    def __init__(self, *arg, **kwargs):
       super(ProductForm, self).__init__(*arg, **kwargs)

       for name, field in self.fields.items():
           field.widget.attrs.update({'class': ''})



class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ['product', 'order', 'quantity']

    def __init__(self, *arg, **kwargs):
       super(OrderItemForm, self).__init__(*arg, **kwargs)


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['customer', 'street', 'state', 'country', 'zipcode', 'card', 'status']

    def __init__(self, *arg, **kwargs):
       super(OrderForm, self).__init__(*arg, **kwargs)



class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name','last_name', 'email', 'phone']
    
    def __init__(self, *arg, **kwargs):
        super(CustomerForm, self).__init__(*arg, **kwargs)