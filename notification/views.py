from django.shortcuts import render
from .models import Notifications
from django.contrib.auth.decorators import login_required
from twitteruser.views import get_recent_users


@login_required()
def notification_view(request):
    notifications = Notifications.objects.filter(user=request.user)
    tweets = []
    for notification in notifications:
        tweet = notification.notification.tweet
        tweets.append(tweet)

    notifications.delete()
    recent_users = get_recent_users()
    context = {
        'tweets': tweets,
        'recent_users': recent_users
    }
    return render(request, 'notification/notifications.html', context)
