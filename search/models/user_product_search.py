from django.db import models

# Create your models here.
class UserProductSearch(models.Model):
    """Model definition for UserProductSearch"""

    user = models.ForeignKey(
        'accounts.User',
        on_delete=models.CASCADE,
    )

    product = models.ForeignKey(
        'product.Product',
        on_delete=models.CASCADE,
    )

    pub_date = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        """Meta definition for UserProductSearch."""

        verbose_name = "UserProductSearch"
        verbose_name_plural = "UserProductSearches"
        db_table = "user_product_searches"
