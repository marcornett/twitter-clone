from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

from twitteruser.views import get_user
from .forms import SignUpForm, LoginForm
from twitteruser.models import TwitterUser
from tweet.models import Tweet
from twitteruser.views import get_recent_users

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        user = get_user(request.user.username)
        followers = user.follow.all()
        follow_list = [request.user]
        for follower in followers:
            follow_list.append(follower)

        tweets = Tweet.objects.filter(
            user__username__in=follow_list).order_by('-date_created')
        recent_users = get_recent_users()
        context = {
            'tweets': tweets,
            'recent_users': recent_users
            }
        return render(request, 'authentication/index.html', context)


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        recent_users = get_recent_users()
        context = {
            'form': form,
            'title': 'Sign Up',
            'recent_users': recent_users
            }
        return render(request, 'authentication/generic_form.html', context)
    
    def post(self, request):
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


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        recent_users = get_recent_users()
        context = {
            'form': form,
            'title': 'Login',
            'recent_users': recent_users
        }
        return render(request, 'authentication/generic_form.html', context)
    
    def post(self, request):
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


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('index')

