from django.db import models
from django.contrib.auth.models import User
import datetime

class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=100)

    class Meta:
        db_table = 'customer'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(default='', blank=True, null=True)
    image = models.ImageField(upload_to='products/')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    class Meta:
        db_table = 'product'
        ordering = ["id"]

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.TextField(default='', null=True, blank=True)
    phone = models.IntegerField(default=0)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.product.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='profiles/', default='profiles/default.jpg')
    joined = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.user.username
