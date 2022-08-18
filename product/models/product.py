from django.db import models

# Create your models clehere.

class Product(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False) # primary key
    category_id = models.ForeignKey('product.Category', null = False, blank = False, on_delete = models.CASCADE)
    name = models.CharField(max_length = 400, null = False, blank = False)
    producer = models.CharField(max_length = 400, null = False, blank = False)
    feedback_cnt = models.IntegerField()
    review_cnt = models.IntegerField()
    visit_cnt = models.IntegerField()
    thumbnail_url = models.URLField(null = True, blank = True)
    rate_sum = models.FloatField(null = True, blank = True)
    rate = models.FloatField()