from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name='region_index'),
    path('new', views.new, name='new_region'),
    path('create', views.create, name='create_region'),
    path('update', views.update, name='update_region'),
    path('<ref>/edit', views.edit, name='edit_region'),
    path('<ref>/delete', views.delete, name='region_delete'),
]