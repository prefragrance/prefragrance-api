from django.db import models
from product.models import Product
from account.models import User

class ProductFeedback(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    product = models.ForeignKey(Product, null = False, blank = False, on_delete = models.CASCADE, related_name="feedbacks")
    user = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE)

    class Meta:
        # 유저가 좋아요 한 제품 중복 방지
        constraints = [
            models.UniqueConstraint(
                fields=["product", "user"],
                name="unique productfeedbacks"
            )
        ]