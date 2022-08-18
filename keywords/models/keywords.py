from django.db import models

# Create your models here.

class Keywords(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False) # primary key
    name = models.CharField(max_length = 200, null = False, blank = False)