from django.db import models
from twitteruser.models import TwitterUser
from tweet.models import Tweet


class Notifications(models.Model):
    notification = models.ForeignKey(Tweet, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, null=True)
