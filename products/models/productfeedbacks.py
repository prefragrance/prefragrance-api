from django.db import models
from products.models import Products
from account.models import User

class ProductFeedbacks(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    product_id = models.ForeignKey(Products, null = False, blank = False, on_delete = models.CASCADE)
    user_id = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE)