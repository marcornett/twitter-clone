from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from twitteruser.views import get_user
from .forms import SignUpForm, LoginForm
from twitteruser.models import TwitterUser
from tweet.models import Tweet


@login_required
def index(request):
    user = get_user(request.user.username)
    followers = user.follow.all()
    follow_list = [request.user]
    for follower in followers:
        follow_list.append(follower)

    tweets = Tweet.objects.filter(
        user__username__in=follow_list).order_by('-date_created')
    context = {'tweets': tweets}
    return render(request, 'authentication/index.html', context)


def sign_up_view(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_user = TwitterUser.objects.create_user(
                username=data['username'],
                password=data['password'],
                display=data['display']
            )
            login(request, new_user)
            return redirect('index')

    context = {'form': form, 'title': 'Sign Up'}
    return render(request, 'authentication/generic_form.html', context)


def login_view(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password']
                )
            if user:
                login(request, user)
                next_page = request.GET['next']
                return HttpResponseRedirect(next_page)

    context = {'form': form, 'title': 'Login'}
    return render(request, 'authentication/generic_form.html', context)


def logout_view(request):
    logout(request)
    return redirect('index')
