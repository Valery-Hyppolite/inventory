


from django.shortcuts import redirect, render
from .models import *

def get_products_left_quantity(request):
    all_products = []
    total_instock = 0
    for q in Product.objects.all():
        all_products.append(q.get_product_instock)
        total_instock = sum(all_products)
    return total_instock

def get_total_profit(request):
    all_profit = []
    total_profit = 0
    for r in Product.objects.all():
        all_profit.append(r.get_profit)
        total_profit = sum(all_profit)
        print(total_profit)
    return total_profit


def get_total_sold(request):
    all_sold = []
    total_sold = 0
    for s in Product.objects.all():
        all_sold.append(s.get_product_sold)
        total_sold = sum(all_sold)
        print(total_sold)
    return total_sold


def get_total_revenue(request):
    total_revenue = []
    total = 0
    for r in Product.objects.all():
        total_revenue.append(r.get_revenue)
        total = sum(total_revenue)
    return total

# from .models import Product
# from django.db.models import Q


# def search_products(request):
#     search_query = ''
#     if request.GET.get('search_query'):
#         search_query = request.GET.get('search_query')

#     products = Product.objects.distinct().filter(Q(item_name__icontains=search_query)| Q(price__icontains=search_query)| Q(item_category__name__icontains=search_query))
#      # object.filter ahoow you to render all objects if query is empty and also render the specific search if there is a serach rquest.
#     return products, search_query