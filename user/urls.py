from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index_user'),
    path('login', views.login_user, name='user_login'),
]
