from django.db import models
from products.models import Products
from products.models import Codes


class ProductCodes(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False) 
    product_id = models.ForeignKey(Products, null = False, blank = False, on_delete = models.CASCADE)
    code_id = models.ForeignKey(Codes, null = False, blank = False, on_delete = models.CASCADE)