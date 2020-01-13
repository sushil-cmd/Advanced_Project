from django.contrib import admin
from .models import OrderItem,Order,Item

admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
