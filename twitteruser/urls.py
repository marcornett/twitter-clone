from django.urls import path
from twitteruser import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('<str:username>/', views.user_view, name='user')
]
