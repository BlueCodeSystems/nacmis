from django.urls import path

from . import views

app_name = 'data_collector_app'

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]