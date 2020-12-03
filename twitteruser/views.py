from django.shortcuts import render, redirect
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required

@login_required()
def profile_view(request):
    user = TwitterUser.objects.get(username=request.user.username)
    tweets = Tweet.objects.filter(user=request.user).order_by('-date_created')
    num_of_following = len(user.follow.all())
    context = {
        'tweets': tweets, 
        'user': user,
        'num_of_following': num_of_following,
        }
    return render(request, 'twitteruser/user.html', context)

def user_view(request, username):
    user = TwitterUser.objects.get(username=username)
    tweets = Tweet.objects.filter(user=user)
    follower = request.user.follow.filter(display=user.display)
    if request.method == 'POST':
        current_user = TwitterUser.objects.get(username=request.user.username)
        if len(follower) > 0:
            current_user.follow.remove(user)
        else:
            current_user.follow.add(user)
        return redirect(f'/user/{username}')
    context = {
        'tweets': tweets,
        'user': user,
        'follower': follower,
    }
    return render(request, 'twitteruser/user.html', context)
