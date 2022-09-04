from django.db import models
from product.models import Product
from tag.models import Tag

class ProductTag(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    product = models.ForeignKey(
        Product, null = False, blank = False, on_delete = models.CASCADE
        )
    tag = models.ForeignKey(
        "tag.Tag", on_delete = models.CASCADE
        )
    cnt = models.IntegerField(
        default=0,
        blank=False,
    )
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["product", "tag"],
                name="unique_product_tag",
            )
        ]

