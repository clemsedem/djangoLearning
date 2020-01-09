from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name='index_cities'),
    path('new', views.new, name='new_city'),
    # path('create', views.create, name='create_city'),
    path('<ref>/delete', views.delete, name='delete_city'),
    path('<ref>/edit', views.edit, name='edit_city'),
]