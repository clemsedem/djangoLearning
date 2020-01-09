from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name='index_suburb'),
    path('new', views.new, name='new_suburb'),
    path('<suburb>/edit', views.edit, name='edit_suburb'),
    path('<suburb>/delete', views.delete, name='delete_suburb'),
]