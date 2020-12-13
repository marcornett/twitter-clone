from django.urls import path
from tweet import views

urlpatterns = [
    path('<int:id>/', views.tweet_view, name='tweet'),
    path('create-tweet/', views.create_tweet, name='create_tweet')
]
