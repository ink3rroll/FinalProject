from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    price = models.IntegerField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

class Seller(models.Model):
    username = models.CharField(max_length=255)
    credit = models.IntegerField(null=True, blank=True)
    products = models.ManyToManyField(Product)

    def __str__(self):
        return self.username

class Buyer(models.Model):
    username = models.CharField(max_length=255)
    credit = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.username

class MOP(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Receipt(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, related_name='receipts')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='receipts')
    mode_of_payment = models.ForeignKey(MOP, on_delete=models.CASCADE, related_name='receipts')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='receipts')
    quantity = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.buyer} bought {self.quantity} {self.product}/s from {self.seller}"
