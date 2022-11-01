from unittest.util import _MAX_LENGTH
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from accounts.models import User


class Review(models.Model):

    class Season(models.TextChoices):
        SPRING = 'SPRING'
        SUMMER = 'SUMMER'
        AUTUMN = 'AUTUMN'
        WINTER = 'WINTER'

    class Time(models.TextChoices):
        DAY = 'DAY'
        NIGHT = 'NIGHT'

    class Duration(models.IntegerChoices):
        LOW = 1
        MID = 2
        HIGH = 3

    class Strength(models.IntegerChoices):
        LOW = 1
        MID = 2
        HIGH = 3

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="사용자")
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name="제품", related_name="reviews")
    season = models.CharField(choices=Season.choices, max_length = 100)
    time = models.CharField(choices=Time.choices, max_length = 100)
    duration = models.IntegerField(choices=Duration.choices)
    strength = models.IntegerField(choices=Strength.choices)
    content = models.CharField(max_length=1500, verbose_name="내용")
    rate = models.FloatField(validators=[MinValueValidator(0,5),MaxValueValidator(5.0)])
    pub_date = models.DateTimeField(auto_now=True, verbose_name="날짜")
    feedback_cnt = models.PositiveIntegerField(default=0)
    liked_users = models.ManyToManyField('accounts.User', through='review.ReviewFeedback', related_name='liked_reviews')
    tags = models.ManyToManyField(
    "tag.Tag",
    related_name="review_tags",
    through="review.ReviewTag",
    )

    def __str__(self):
        return self.content

    class Meta:
        db_table = "review"
        verbose_name = "Review"
        verbose_name_plural = "Review"