from django.db import models
# Create your models here.

class Code(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False)
    name = models.CharField(unique=True,max_length = 100, null = False, blank = False)