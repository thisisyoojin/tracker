from django.contrib import admin
from tracker.models import Inventory, Item, Order, Supplier

admin.site.register(Item)
admin.site.register(Inventory)
admin.site.register(Order)
admin.site.register(Supplier)
