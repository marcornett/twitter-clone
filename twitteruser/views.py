from django.shortcuts import render
from tweet.models import Tweet
from twitteruser.models import TwitterUser
from django.contrib.auth.decorators import login_required

@login_required()
def profile_view(request):
    user = TwitterUser.objects.get(username=request.user.username)
    tweets = Tweet.objects.filter(user=request.user).order_by('-date_created')
    context = {'tweets': tweets, 'user': user}
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
    context = {
        'tweets': tweets,
        'user': user,
        'follower': follower,
        # 'num_of_followers': num_of_followers,
    }
    return render(request, 'twitteruser/user.html', context)
