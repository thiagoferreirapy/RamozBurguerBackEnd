from django.db import models
from uuid import uuid4
import hashlib


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name.upper()
    
def upload_image(instance, filename):
    hash_instance = hashlib.sha256(str(instance.id).encode())
    hashed_filename = hash_instance.hexdigest() + '-' + filename
    return hashed_filename

class Products(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    ingredients = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='product_category')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to=upload_image, blank=True, null=True)

    def __str__(self):
        return self.name.upper()
    


NACIONALITY_CHOICES = (
    ('MEAT', 'Adicional de Carne'),
    ('SAUCE', 'Adicional de Molho'),
)

class AdditionalFree(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=155)
    description = models.TextField(blank=True, null=True)
    category_type = models.CharField(max_length=100, choices=NACIONALITY_CHOICES, null=True, blank=True)

    def __str__(self):
        return self.name.upper()
    
class BagProduct(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    product_id = models.ForeignKey(Products, on_delete=models.PROTECT, related_name='product_bag')
    additional_meat = models.ForeignKey(AdditionalFree, on_delete=models.PROTECT, related_name='additional_meat_bag', blank=True, null=True)
    additional_sauce = models.ForeignKey(AdditionalFree, on_delete=models.PROTECT, related_name='additional_sauce_bag', blank=True, null=True)
    quantity = models.IntegerField()
    observation = models.CharField(max_length=255, blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2)
    finished = models.BooleanField(default=False)

    def __str__(self):
        return self.product_id.name.upper()