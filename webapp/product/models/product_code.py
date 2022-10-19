from django.db import models
from product.models import Product, Code

class ProductCode(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    product = models.ForeignKey(Product, null = False, blank = False, on_delete = models.CASCADE)
    code = models.ForeignKey(Code, null = False, blank = False, on_delete = models.CASCADE)

    class Meta:
        # 하나의 코드가 어떤 product 가 중복되지 않도록
        constraints = [
            models.UniqueConstraint(
                fields=["product", "code"],
                name="unique_product_code",
            )
        ]