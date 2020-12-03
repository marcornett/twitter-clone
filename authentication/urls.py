from django.urls import path
from authentication import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.sign_up_view, name='sign_up'),
    path('logout/', views.logout_view, name='logout')
]
