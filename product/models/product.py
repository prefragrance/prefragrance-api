from django.db import models

# Create your models clehere.

class Product(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False) # primary key
    category = models.ForeignKey('product.Category', null = False, blank = False, on_delete = models.CASCADE)
    name = models.CharField(max_length = 400, null = False, blank = False)
    producer = models.CharField(max_length = 400, null = False, blank = False)
    feedback_cnt = models.IntegerField(default=0)
    review_cnt = models.IntegerField(default=0)
    visit_cnt = models.IntegerField(default=0)
    thumbnail_url = models.URLField(null = True, blank = True)
    rate_sum = models.FloatField(default=0)
    rate = models.FloatField(default=0)
    liked_users = models.ManyToManyField('account.User', through='product.ProductFeedback', related_name='liked_products')

    def __str__(self):
        return self.name