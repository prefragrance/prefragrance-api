from django.db import models
from keywords.models import Keyword
from .reviews import Review

class ReviewKeyword(models.Model):
    keyword_id = models.ForeignKey(Keyword, on_delete=models.CASCADE, verbose_name="키워드")
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE, verbose_name="리뷰")

    class Meta:
        db_table = "review_keywords"
        verbose_name = "Review Keyword"
        verbose_name_plural = "Review Keyword"