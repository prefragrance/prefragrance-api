from django.db import models
from tag.models import Tag
from .review import Review

class ReviewTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name="키워드")
    review = models.ForeignKey(Review, on_delete=models.CASCADE, verbose_name="리뷰")

    class Meta:
        db_table = "review_tag"
        verbose_name = "Review Tag"
        verbose_name_plural = "Review Tag"
        # 하나의 리뷰에 중복된 태그가 없도록
        constraints = [
            models.UniqueConstraint(
                fields=["review", "tag"],
                name="unique_review_tag",
            )
        ]