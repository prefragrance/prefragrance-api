from django.db import models

# Create your models clehere.

class Product(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False) # primary key
    category = models.ForeignKey('product.Category', null = False, blank = False, on_delete = models.CASCADE)
    name = models.CharField(max_length = 400, null = False, blank = False)
    producer = models.CharField(max_length = 400, null = False, blank = False)
    tags = models.ManyToManyField(
    "tag.Tag",
    related_name="tags",
    through="product.ProductTag",
)
    feedback_cnt = models.IntegerField()
    review_cnt = models.IntegerField()
    visit_cnt = models.IntegerField()
    thumbnail_url = models.URLField(null = True, blank = True)
    rate_sum = models.FloatField(null = True, blank = True)
    rate = models.FloatField()
    liked_users = models.ManyToManyField('accounts.User', through='product.ProductFeedback', related_name='liked_products')

    def __str__(self):
        return self.name


