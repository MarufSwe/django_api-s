from django.db import models


# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='category_images')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.errors = None

    def __str__(self):
        return self.category_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.CharField(max_length=15)
    quantity = models.CharField(max_length=15)
    in_stock = models.CharField(max_length=25)
    supplier_name = models.CharField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.errors = None

    def __str__(self):
        return self.product_name


class Order(models.Model):
    customer_name = models.CharField(max_length=40)
    order_date = models.DateField()
    shipping_date = models.DateField()
    shipping_address = models.TextField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.errors = None

    def __str__(self):
        return self.customer_name


class OrderDetails(models.Model):
    price = models.CharField(max_length=35)
    quantity = models.CharField(max_length=35)
    discount = models.CharField(max_length=50)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.price
