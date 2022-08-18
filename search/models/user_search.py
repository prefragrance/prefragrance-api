from django.db import models

# Create your models here.
class UserSearch(models.Model):
    """Model definition for UserSearch"""

    user = models.ForeignKey(
        'account.User',
        on_delete=models.CASCADE,
    )

    search = models.ForeignKey(
        'search.Search',
        on_delete=models.CASCADE,
    )

    pub_date = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        """Meta definition for UserSearch."""

        verbose_name = "UserSearch"
        verbose_name_plural = "UserSearches"
        db_table = "user_searches"
