from django.db import models
from product.models import Product
from tag.models import Tag

class ProductTag(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    product_id = models.ForeignKey(Product, null = False, blank = False, on_delete = models.CASCADE)
    tag_id = models.ForeignKey("tag.Tag", on_delete = models.CASCADE)