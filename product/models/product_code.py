from django.db import models
from product.models import Product, Code

class ProductCode(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False) 
    product = models.ForeignKey(Product, null = False, blank = False, on_delete = models.CASCADE)
    code = models.ForeignKey(Code, null = False, blank = False, on_delete = models.CASCADE)
