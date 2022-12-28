from django.db import models
from product.models import Product, Code

class ProductCode(models.Model):
        
    id = models.AutoField(primary_key=True, null=False, blank=False)
    product = models.ForeignKey(Product, null = False, blank = False, on_delete = models.CASCADE)
    code = models.ForeignKey(Code, null = False, blank = False, on_delete = models.CASCADE)

    class Meta:
        # 하나의 코드가 어떤 product 가 중복되지 않도록
        constraints = [
            models.UniqueConstraint(
                fields=["product", "code"],
                name="unique_product_code",
            )
        ]
        
'''
choicefield 참고용 리뷰 모델
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

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="사용자")
    product = models.ForeignKey(
        "product.Product",
        on_delete=models.CASCADE,
        verbose_name="제품",
        related_name="reviews",
    )
    season = models.IntegerField(choices=Season.choices)
    time = models.IntegerField(choices=Time.choices)
    duration = models.IntegerField(choices=Duration.choices)
    strength = models.IntegerField(choices=Strength.choices)
    content = models.CharField(max_length=1500, verbose_name="내용")
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    pub_date = models.DateTimeField(auto_now=True, verbose_name="날짜")
    feedback_cnt = models.PositiveIntegerField(default=0)
    liked_users = models.ManyToManyField(
        "accounts.User", through="review.ReviewFeedback", related_name="liked_reviews"
    )
    tags = TaggableManager(blank=True)





'''