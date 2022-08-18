from django.db import models
from products.models import Product
from keywords.models import Keyword

class ProductKeyword(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    product_id = models.ForeignKey(Product, null = False, blank = False, on_delete = models.CASCADE)
    keyword_id = models.ForeignKey(Keyword, on_delete = models.CASCADE)