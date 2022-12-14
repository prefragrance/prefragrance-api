from django.db import models
from django.db.models import Sum
from taggit.managers import TaggableManager

from review.models import Review


class Product(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)  # primary key
    category = models.ForeignKey(
        "product.Category", null=False, blank=False, on_delete=models.CASCADE
    )
    name = models.CharField(max_length=400, null=False, blank=False)
    producer = models.CharField(max_length=400, null=False, blank=False)
    tags = TaggableManager(blank=True)
    codes = models.ManyToManyField(
        "product.Code",
        related_name="codes",
        through="product.ProductCode",
    )
    feedback_cnt = models.IntegerField(default=0)
    review_cnt = models.IntegerField(default=0)
    visit_cnt = models.IntegerField(default=0)
    thumbnail_url = models.URLField(null=True, blank=True)
    rate_sum = models.FloatField(null=True, blank=True)
    rate = models.FloatField(default=0)
    liked_users = models.ManyToManyField(
        "accounts.User",
        through="product.ProductFeedback",
        related_name="liked_products",
    )

    def __str__(self):
        return self.name

    def reset_product_review_cnt_and_rate(self):
        self.review_cnt = Review.objects.filter(product=self).count()
        rate_sum = self.reviews.aggregate(Sum("rate"))
        self.rate_sum = rate_sum["rate__sum"]
        self.rate = self.rate_sum / self.review_cnt
        self.save()
