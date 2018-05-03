from django.urls import include, path

from . import views

app_name = 'data_entry'

from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_clean_model, name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('select2/', include('django_select2.urls'))    # for select2 
]