from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/regions', views.index, name='regions'),
]