from django.shortcuts import render
from .models import Notifications
from django.contrib.auth.decorators import login_required

def notification_view(request):
    notifications = Notifications.objects.filter(user=request.user)
    tweets = []
    for notification in notifications:
        tweet = notification.notification.tweet
        tweets.append(tweet)

    notifications.delete()
    context = {'tweets': tweets}
    return render(request, 'notification/notifications.html', context)
    
