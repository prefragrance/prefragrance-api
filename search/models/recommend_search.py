from django.db import models

# Create your models here.
class RecommendSearch(models.Model):
    """Model definition for RecommendSearch"""

    content = models.CharField(
        max_length=30,
    )

    class Meta:
        """Meta definition for RecommendSearch."""

        verbose_name = "RecommendSearch"
        verbose_name_plural = "RecommendSearches"
        db_table = "recommend_searches"
