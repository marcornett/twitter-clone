from django.shortcuts import render, redirect
from .models import Tweet
from .forms import TweetForm
from twitteruser.models import TwitterUser
from notification.models import Notifications

from django.contrib.auth.decorators import login_required
import re


def tweet_view(request, id):
    tweet = Tweet.objects.get(id=id)
    recent_users = TwitterUser.objects.all().order_by('-id')[:5]
    context = {
        'tweet': tweet,
        'recent_users': recent_users
    }
    return render(request, 'tweet/tweet.html', context)


@login_required()
def create_tweet(request):
    form = TweetForm()
    # Couldn't import get_recent_users(), throws error: 
    # cannot import name 'get_recent_users' from partially initialized module
    # 'twitteruser.views' (most likely due to a circular import)
    recent_users = TwitterUser.objects.all().order_by('-id')[:5]
    
    if request.method == 'POST':
        form = TweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            tweet = data['tweet']
            pattern = re.compile(r'@(\w+)')
            names = pattern.findall(tweet)
            tweet_model = Tweet.objects.create(
                user=request.user,
                tweet=data['tweet']
            )
            for name in names:
                is_user = TwitterUser.objects.filter(display=name)
                if is_user:
                    user = TwitterUser.objects.get(display=name)
                    Notifications.objects.create(
                        user=user,
                        notification=tweet_model
                        )
            return redirect('/')
    # recent_users = get_recent_users()
    title = 'Post Tweet'
    context = {
        'form': form,
        'title': title,
        'recent_users': recent_users
    }
    return render(request, 'authentication/generic_form.html', context)


def filter_tweets(user):
    tweets = Tweet.objects.filter(user=user)
    return tweets
    