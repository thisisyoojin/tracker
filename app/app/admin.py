from django.contrib import admin
from tracker.models import InventoryLog, Item, Order, Supplier

admin.site.register(Item)
admin.site.register(InventoryLog)
admin.site.register(Order)
admin.site.register(Supplier)
