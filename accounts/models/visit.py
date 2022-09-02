from django.db import models

# Create your models here.
class Visit(models.Model):
    """Model definition for Visit"""

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
        """Meta definition for Visit."""

        verbose_name = "Visit"
        verbose_name_plural = "Visits"
        db_table = "visits"

