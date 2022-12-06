from django.db import models

class ReviewCount(models.Model):
    gold_medal = models.IntegerField()
    silver_medal = models.IntegerField()
    bronze_medal = models.IntegerField()

    class Meta:
        db_table = "review_count"
        verbose_name = "Review Count"
        verbose_name_plural = "Review Counts"
