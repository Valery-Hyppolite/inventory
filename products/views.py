
from multiprocessing import context
from django.shortcuts import redirect, render
from .models import Product, Order, Customer, OrderItem, Shipping
from .form import ProductForm, CustomerForm, OrderItemForm, OrderForm, ShippingForm
from django.db.models import Q
from .search_query import get_products_left_quantity, get_total_profit, get_total_sold, get_total_revenue

#-----------------------------------VIEW ITEMS IN THE SYSTEM----------------------------------------------
def view_new_orders(request):
    """SHOW AL RECENT ORDERS & SUMMARY OF SALES, PROFITS, AND REVENUE"""
    orders = Order.objects.all()
    total_instock = get_products_left_quantity(request)
    total_profit = get_total_profit(request)
    total_sold =get_total_sold(request)
    total_revenue = get_total_revenue(request)

    context = {'orders': orders, 'all_products':total_instock, 'total_profit':total_profit, 'total_sold': total_sold, 'total_revenue':total_revenue}   
    return render(request, 'dashboard.html', context)


def view_order(request, pk):
    """SHOW ORDER DETAILS"""
    order = Order.objects.get(id=pk)
    shipping = Shipping.objects.get(id=pk)
    order_items = order.orderitem_set.all()
    

    context = {'orderitems': order_items, 'order':order, 'shipping':shipping}
    return render(request, 'order.html', context)


def customer(request, pk):
    """SHOW CUSTOMER ORDERS/ORDER HISTORY"""
    customer = Customer.objects.get(id=pk)
    customer_orders = customer.order_set.all()

    contex = {'customer': customer, 'orders': customer_orders}
    return render(request,'customer.html', contex)


def orders(request):
    """SHOW ALL ORDERS"""
    orders = Order.objects.all()
    contex = {'orders': orders}
    return render(request,'orders.html', contex)


def customers(request):
    """SHOW ALL CUSTOMERS"""
    customers = Customer.objects.all()
    contex = {'customers': customers}
    return render(request,'customers.html', contex)


def products(request):
    """SHOW ALL PRODUCTS"""
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products.html', context)


def product(request, pk):
    """SHOW SINGLE PRODUT DETAILS"""
    product = Product.objects.get(id=pk)
    orderitems = product.orderitem_set.all()
    context = {'product': product, 'orderitems':orderitems}
    return render(request, 'single-product.html', context)


#-------------------------------------ADDING ITEM SECTION--------------------------------
def add_product(request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    
    context = {'form': form}
    return render(request, 'form.html', context)


def add_customer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customers')
    
    context = {'form': form}
    return render(request, 'customer_form.html', context)


def add_orderitem(request):
    form = OrderItemForm()
    if request.method == 'POST':
        form = OrderItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
    
    context = {'form': form}
    return render(request, 'order_form.html', context)


def add_order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('orders')
    
    context = {'form': form}
    return render(request, 'order_form.html', context)

#-------------------------------------UPDATE & DELETE ITEM SECTION--------------------------------

def update_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return  redirect('products')
    context = {'form': form, 'header': 'update'}
    return render(request, 'form.html', context)


def delete_product(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)

    if request.method == 'POST':
            product.delete()
            return  redirect('products')
    context = {'form': form,  'header': 'delete'}
    return render(request, 'form.html', context)


def update_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customers')
    
    context = {'form': form, 'header': 'update'}
    return render(request, 'customer_form.html', context)

def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        customer.delete()
        return redirect('customers')
    
    context = {'form': form, 'header': 'delete'}
    return render(request, 'customer_form.html', context)


def update_order(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        if form.is_valid(): 
            form.save() 
            return redirect('orders')
    context = {'form': form, 'header': "update"}
    return render(request, 'order_form.html', context)


def update_orderitem(request, pk):
    order_item = OrderItem.objects.get(id=pk)
    form = OrderItemForm(instance=order_item)

    if request.method == 'POST':
        form = OrderItemForm(request.POST, instance=order_item)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context = {'form': form,'header': "update"}
    return render(request, 'order_form.html', context)

def update_shipping(request, pk):
    shipping = Shipping.objects.get(id=pk)
    form = ShippingForm(instance=shipping)

    if request.method == 'POST':
        form = ShippingForm(request.POST, instance=shipping)
        if form.is_valid():
            form.save()
            return redirect('orders')
    context = {'form': form,'header': "update"}
    return render(request, 'order_form.html', context)





#------------------view and search for products section --------------------------------
# def view_products(request):
#     products, search_query = search_products(request)
   
#     # products = Product.objects.all()
#     context = {'products': products, 'search_query': search_query}
#     return render(request, 'dashboard.html', context)














#################################STOP HERE, NOT PART OF THE CODE, IGNORE THE REST###################
###############======================================================#################################
#-------------------------------------ADD PRODUCTS -------------------------------------------

# def add_product(request):
#     form = ProductForm()

#     if request.method == 'POST':
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return  redirect('products')
#     context = {'form': form,  'header': 'add'}
#     return render(request, 'form.html', context)




#-------------------------------------EDIT PRODUCTS -------------------------------------------

# def update_product(request, pk):
#     product = Product.objects.get(id=pk)
#     form = ProductForm(instance=product)

#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance=product)
#         if form.is_valid():
#             form.save()
#             return  redirect('products')
#     context = {'form': form, 'header': 'update'}
#     return render(request, 'form.html', context)



#-------------------------------------DELETE PRODUCTS -------------------------------------------

# def delete_product(request, pk):
#     product = Product.objects.get(id=pk)
#     form = ProductForm(instance=product)

#     if request.method == 'POST':
#             product.delete()
#             return  redirect('products')
#     context = {'form': form,  'header': 'delete'}
#     return render(request, 'form.html', context)

#-------------------------------------single PRODUCT -------------------------------------------
# def view_product(request, pk):
#     product = Product.objects.get(id=pk)
#     context = {'product': product}
#     return render(request, 'single-product.html', context)