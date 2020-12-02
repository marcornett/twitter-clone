from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from .forms import SignUpForm, LoginForm
from twitteruser.models import TwitterUser
from tweet.models import Tweet

@login_required
def index(request):
    # tweets = Tweet.objects.filter(user=request.user).order_by('-date_created')

    user = TwitterUser.objects.get(username=request.user.username)
    followers = user.follow
    # breakpoint()
    tweets = Tweet.objects.filter(user__username__in=[followers])
    # TODO: List at all tweets from current user and all users the user is following
    # TODO: https://stackoverflow.com/questions/9410647/how-to-filter-model-results-for-multiple-values-for-a-many-to-many-field-in-djan
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
