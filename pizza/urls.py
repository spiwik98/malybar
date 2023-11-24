from django.urls import path
from pizza import views

app_name = 'pizza'
urlpatterns = [
    path('', views.index, name='pizza_index'),
]

