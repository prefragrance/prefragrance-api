from django.db import models
from products.models import Products
from keywords.models import Keywords

class ProductKeywords(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    product_id = models.ForeignKey(Products, null = False, blank = False, on_delete = models.CASCADE)
    keyword_id = models.ForeignKey(Keywords, on_delete = models.CASCADE)