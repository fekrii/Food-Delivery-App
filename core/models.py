from django.db import models
from _auth.models import CustomerProfile, ResturantProfile


class Product(models.Model):
    name = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    class Status(models.TextChoices):
        ORDERED = "ORDERED", "Ordered"
        INPROGRESS = "INPROGRESS", "In progress"
        DONE = "DONE", "Done"
        WITHDRIVER = "WITHDRIVER", "With Driver"
        DELIVERED = "DELIVERED", "Delivered"
        CANCELED = "CANCELED", "Cancelled"


    base_role = Status.INPROGRESS

    
    name = models.CharField(max_length=255)
    ordered_by = models.ForeignKey(CustomerProfile, related_name='order_by',on_delete=models.CASCADE)
    resturant = models.ForeignKey(ResturantProfile, related_name='order_resturant',on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, related_name='order_products')
    status = models.CharField(max_length=50, choices=Status.choices, default=Status.ORDERED)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return str(self.name)





class Menu(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, related_name='menu_products')
    resturant = models.ForeignKey(ResturantProfile, related_name='menu_resturant',on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return str(self.name)