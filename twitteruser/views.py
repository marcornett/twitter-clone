from django.shortcuts import render, redirect
from twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required
from tweet.views import filter_tweets


@login_required()
def profile_view(request):
    user = get_user(request.user.username)
    tweets = filter_tweets(request.user).order_by('-date_created')
    num_of_following = len(user.follow.all())
    recent_users = get_recent_users()
    # breakpoint()
    context = {
        'tweets': tweets,
        'user': user,
        'num_of_following': num_of_following,
        'recent_users': recent_users,
        }
    return render(request, 'twitteruser/user.html', context)


def user_view(request, username):
    user = get_user(username)
    tweets = filter_tweets(user)
    follower = None
    if request.user.is_authenticated:
        follower = request.user.follow.filter(display=user.display)
    if request.method == 'POST':
        current_user = get_user(request.user.username)
        if len(follower) > 0:
            current_user.follow.remove(user)
        else:
            current_user.follow.add(user)
        return redirect(f'/user/{username}')
    recent_users = get_recent_users()
    context = {
        'tweets': tweets,
        'user': user,
        'follower': follower,
        'recent_users': recent_users,
    }
    return render(request, 'twitteruser/user.html', context)


def get_user(username):
    user = TwitterUser.objects.get(username=username)
    return user


def get_recent_users():
    users = TwitterUser.objects.all().order_by('-id')[:5]
    return users
