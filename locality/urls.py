from django.urls import  path
from . import views

urlpatterns = [
    path('', views.index, name='index_localities'),
    path('new', views.new, name='new_locality'),
    path('<locality>/edit', views.edit, name='edit_locality'),
    path('<locality>/delete', views.delete, name='delete_locality'),
]