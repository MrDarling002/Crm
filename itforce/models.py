from django.db import models
from django.db.models.deletion import CASCADE,PROTECT
from django.db.models.fields import DurationField
from datetime import date, time
from django.utils import timezone
from django.contrib.auth.models import User


class OrderStatus(models.Model):
    time=models.CharField(max_length=255)
    date=models.DateTimeField(default=timezone.now)

class Customer(models.Model):
    name=models.CharField(max_length=255)
    phone=models.IntegerField(blank=True,null=True)
    date=models.DateTimeField(default=timezone.now)

class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

class ProductCategory(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)

    # Example: Phone, PC, Laptop

class ProductBrand(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    
    # Example: Samsung, Apple, Mi

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.PROTECT)
    product_brand = models.ForeignKey(ProductBrand, on_delete=models.PROTECT)
    serial_number = models.IntegerField(max_length=255)
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    additional_info = models.TextField()
    archived = models.BooleanField(default=False)
    status = models.ForeignKey(OrderStatus, on_delete=models.CASCADE)

