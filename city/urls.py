from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name='index_cities'),
    path('new', views.new, name='new_city'),
    path('create', views.create, name='create_city'),
]