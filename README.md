class Catagory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True )

    def __str__(self):
        return self.name


class Product(models.Model):
    category     = models.ForeignKey(Catagory,null=True, blank=True, on_delete=models.SET_NULL)
    name         = models.CharField(max_length=200, blank=False, null=False)
    price        = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False)
    quantity     = models.IntegerField(null=False, blank=False)
    total_cost   = models.DecimalField(max_digits=9, decimal_places=2, blank=False, null=False)
    stock_date   = models.DateField(auto_now=True)

    def __str__(self):
        return self.name

    #---------------------PER PRODUCT CALCULATIONS OF PRODUCTS INVENTORY------------------------
    @property
    def get_product_sold(self):
        """for each product that is sold, calculate the total sold"""
        sold = 0
        orderitems = self.orderitem_set.all()
        for item in orderitems:
            if item.product.id == self.id:
                sold = self.quantity - self.get_product_instock
        return sold

    @property
    def get_product_instock(self):
        """for each product that was sold, calculate the total the quantity left in store"""
        current_stock = self.quantity
        orderitems = self.orderitem_set.all()
        sold_items = []
        for item in orderitems:
            if item.product.id == self.id:
                sold_items.append(item.quantity)
                current_stock = self.quantity - sum(sold_items)
                # self.quantity = self.quantity - item.quantity
        return current_stock

    @property
    def get_revenue(self):
        revenue = 0
        cost_per_item = self.total_cost/self.quantity
        orderitem = self.orderitem_set.all()
        products = []
        for item in orderitem:
            products.append(item.quantity)
            print(f"products: {products}")
            revenue = self.price * sum(products)
            print(f"revenue: {revenue}")
        return revenue

    @property
    def get_profit(self):
        profit = 0
        cost_per_item = self.total_cost/self.quantity
        orderitem = self.orderitem_set.all()
        # profit = sum([(item.get_revenue -sum(item)) for item in orderitem])
        products = []
        for item in orderitem:
            products.append(item.quantity)
            print(f"products: {products}")
            pre_revenue = self.price * sum(products)
            profit = pre_revenue - (cost_per_item * sum(products))
            print(f"pre revenue: {pre_revenue}")
            print(f"profit: {profit}")
        return profit
        
    # -----------------TOTAL CALCULATION OF PRODUCTS INVENTOTY ---------------------------   
    
    
class Customer(models.Model):
    first_name   = models.CharField(max_length=60, blank=False, null=False)
    last_name    = models.CharField(max_length=60, blank=False, null=False)
    email        = models.EmailField(blank=False, null=False)
    phone        = models.CharField(max_length=10,  blank=True, null=True)

    def __str__(self):
        return self.first_name

    @property 
    def get_customer_orders(self):
        orders = self.order_set.all()
        total_orders = len([order.id for order in orders])
        return total_orders

    
                    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    street   = models.CharField(max_length=500, blank=False, null=False)
    state    = models.CharField(max_length=200, blank=True, null=True)
    country  = models.CharField(max_length=200, blank=False, null=False)
    zipcode  = models.CharField(max_length=200, blank=True, null=True)
    card     = models.DecimalField(max_digits=4, decimal_places=0, blank=False, null=False, default=4567)
    date     = models.DateField(auto_now=True)
    choices  = (
        ('PROCESSING', 'processing'),
        ('FUFILLED', 'fufilled'),
        ('SHIPPED', 'shipped'),
        ('DELIVERED', 'Archived')
    )
    status = models.CharField(max_length=20, choices=choices, default='DELIVERED')

    def __str__(self):
        return str(self.id)
    
    @property
    def get_total_item(self):
        """for each order, get the total quantity of orderitems"""
        total_quantity = 0
        orderitems = self.orderitem_set.all()
        total_quantity = sum([(item.quantity) for item in orderitems])
        return total_quantity

    @property
    def get_total_total(self):
        """for each oder, sum the total orderitem total price. sum the get_total price"""
        total = 0
        orderitems = self.orderitem_set.all()
        total = sum([(item.get_total) for item in orderitems ])
        return total

    
class OrderItem(models.Model):
     product  = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
     order  = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
     quantity = models.IntegerField(null=False, blank=False, default=1)

     @property
     def get_total(self):
         """for each orderitem created, calculate the total price"""
         total = 0
         total = self.quantity * self.product.price
         return total


     def __str__(self):
        return self.product.name
