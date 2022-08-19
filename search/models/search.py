from django.db import models

# Create your models here.
class Search(models.Model):
    """Model definition for Search"""

    content = models.CharField(
        max_length=30,
        unique=True,
    )

    cnt = models.IntegerField(
        default=0,
        blank=False,
    )
    def __str__(self):
        return self.content

    class Meta:
        """Meta definition for Search."""

        verbose_name = "Search"
        verbose_name_plural = "Searches"
        db_table = "searches"
