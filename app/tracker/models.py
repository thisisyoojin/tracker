import uuid
from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):

    class Category(models.TextChoices):
        FREEZER = 'fz', 'Freezer'
        FRIDGE = 'fr', 'Fridge'
        DRY_ITEM = 'di', 'Dry item'
        SERVER_ZONE = 'sz', 'Server zone'
        ETC = 'et', 'Etc'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=300)
    category = models.CharField(
        max_length=2, choices=Category.choices, null=True, blank=True)
    min_qty = models.SmallIntegerField()
    suppliers = models.ManyToManyField(to="Supplier")
    check_in_Thursday = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class InventoryLog(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
    item_id = models.ForeignKey(to="Item", on_delete=models.CASCADE)
    stock = models.SmallIntegerField()
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.item_id}: {self.stock} ({self.created_at})"


class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, db_index=True)
    item_id = models.ForeignKey(to="Item", on_delete=models.CASCADE)
    item_qty = models.SmallIntegerField()
    item_price = models.FloatField()
    supplier_id = models.ForeignKey(to="Supplier", on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Supplier(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name
