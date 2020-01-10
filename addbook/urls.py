from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('addressbook.urls')),
    path('regions/', include('region.urls')),
    path('cities/', include('city.urls')),
    path('localities/', include('locality.urls')),
    path('suburbs/', include('suburb.urls')),
    path('users/', include('user.urls')),
]
