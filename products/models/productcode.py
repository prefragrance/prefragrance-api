from django.db import models
from products.models import Product, Code

class ProductCode(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False) 
    product_id = models.ForeignKey(Product, null = False, blank = False, on_delete = models.CASCADE)
    code_id = models.ForeignKey(Code, null = False, blank = False, on_delete = models.CASCADE)
