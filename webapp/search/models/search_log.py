from django.db import models

# Create your models here.
# 검색의 로그를 위한 모델

class SearchLog(models.Model):
    """Model definition for SearchLog"""

    content = models.CharField(
        max_length=30,
    )

    pub_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.content

    class Meta:
        """Meta definition for SearchLog."""

        verbose_name = "SearchLog"
        verbose_name_plural = "SearchLogs"
        db_table = "search_logs"
