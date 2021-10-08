from django.db import models
from  django.conf import settings

class Tweet(models.Model):
    """Tweets model."""
    tweet = models.TextField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.date
