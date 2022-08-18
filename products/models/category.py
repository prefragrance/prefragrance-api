from django.db import models

class Category(models.Model):
    id = models.AutoField(primary_key=True, null=False, blank=False) # primary key
    name = models.CharField(max_length = 200, null = False, blank = False)

    def __str__(self):
        return self.name