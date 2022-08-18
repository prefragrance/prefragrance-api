from django.db import models

# Create your models here.
class Search(models.Model):
    """Model definition for Search"""

    content = models.CharField(
        max_length=30,
    )

    cnt = models.IntegerField(
        default=0,
        blank=False,
    )

    class Meta:
        """Meta definition for Search."""

        verbose_name = "Search"
        verbose_name_plural = "Searches"
        db_table = "searches"
