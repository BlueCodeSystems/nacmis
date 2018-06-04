from django.urls import include, path

from . import views

app_name = 'data_entry'

urlpatterns = [
    #path('', views.get_nameinmodel, name='index'),
    path('', views.myform_test, name='index'),
    path('login/', views.Login.as_view(), name='login'),
]