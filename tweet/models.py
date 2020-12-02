from django.db import models
from twitteruser.models import TwitterUser
from django.utils import timezone


class Tweet(models.Model):
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, null=True)
    tweet = models.CharField(
        max_length=140,
        help_text='Tweets are limited to 140 characters.',
        blank=True
    )
    date_created = models.DateTimeField(
        default=timezone.now,
        auto_now_add=False
    )
