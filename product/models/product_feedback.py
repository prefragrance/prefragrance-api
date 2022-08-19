from django.db import models
from product.models import Product
from account.models import User

class ProductFeedback(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    product = models.ForeignKey(Product, null = False, blank = False, on_delete = models.CASCADE)
    user = models.ForeignKey(User, null = False, blank = False, on_delete = models.CASCADE)