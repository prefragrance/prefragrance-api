from django.db import models
from accounts.models import User
from .review import Review

class ReviewFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="사용자")
    review = models.ForeignKey(Review, on_delete=models.CASCADE, verbose_name="리뷰")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="날짜")

    class Meta:
        db_table = "review_feedback"
        verbose_name = "Review Feedback"
        verbose_name_plural = "Review Feedback"
        # 유저가 좋아요 한 리뷰 중복 방지
        constraints = [
            models.UniqueConstraint(
                fields=["user", "review"],
                name="unique reviewfeedbacks"
            )
        ]