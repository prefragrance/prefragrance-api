from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from account.models import User
from product.models import Product


class Review(models.Model):

    class Season(models.IntegerChoices):
        SPRING = 1
        SUMMER = 2
        AUTUMN = 3
        WINTER = 4
    
    class Time(models.IntegerChoices):
        DAY = 1
        NIGHT = 2
    
    class Duration(models.IntegerChoices):
        LOW = 1
        MID = 2
        HIGH = 3

    class Strength(models.IntegerChoices):
        LOW = 1
        MID = 2
        HIGH = 3

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="사용자")
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="제품")
    season = models.IntegerField(choices=Season.choices)
    time = models.IntegerField(choices=Time.choices)
    duration = models.IntegerField(choices=Duration.choices)
    strength = models.IntegerField(choices=Strength.choices)
    content = models.CharField(max_length=1500, verbose_name="내용")
    rate = models.FloatField(validators=[MinValueValidator(0,5),MaxValueValidator(5.0)])
    pub_date = models.DateTimeField(auto_now=True, verbose_name="날짜")
    feedback_cnt = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = "review"
        verbose_name = "Review"
        verbose_name_plural = "Review"