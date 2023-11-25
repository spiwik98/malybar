from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pizza.urls')),
    path('pizza/', include('pizza.urls')),
    path('konta/', include('registration.backends.simple.urls')),
    path('admin/', admin.site.urls),
]
