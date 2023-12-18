from django.contrib import admin
from .models import Seller, Product, Buyer, MOP, Receipt

# Register your models here.

admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(Buyer)
admin.site.register(MOP)
admin.site.register(Receipt)