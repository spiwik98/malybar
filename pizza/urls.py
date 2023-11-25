from django.contrib.auth.decorators import login_required
from django.urls import path
from django.views.generic.list import ListView
from . import views
from .models import Pizza

urlpatterns = [
    path(r'^$', views.index, name='index'),
    path(r'^lista/', login_required(ListView.as_view(model=Pizza)),
        name='lista'),
]

