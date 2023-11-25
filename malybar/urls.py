from django.urls import path
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [
    path('', include('pizza.urls')),
    path('admin/', admin.site.urls),
]
