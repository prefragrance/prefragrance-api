from django.db import models
from account.models import User
from .review import Review

class ReviewFeedback(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="사용자")
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE, verbose_name="리뷰")
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="날짜")

    class Meta:
        db_table = "review_feedbacks"
        verbose_name = "Review Feedback"
        verbose_name_plural = "Review Feedback"