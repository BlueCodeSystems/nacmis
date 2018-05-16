"""nacmis_online URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, path
from django.contrib import admin
from data_entry.views import SupportFieldAutocomplete, OrganizationTargetAutocomplete, \
    DistrictAutocomplete, WardAutocomplete

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data_entry/', include('data_entry.data_urls')),
    path('select2/', include('django_select2.urls')),    # for select2
    path('supportfield-autocomplete/', SupportFieldAutocomplete.as_view(), 
        name='supportfield-autocomplete'),
    path('organizationtarget-autocomplete/', OrganizationTargetAutocomplete.as_view(), 
        name='organizationtarget-autocomplete'),
    path('district-autocomplete/', DistrictAutocomplete.as_view(), name='district-autocomplete'),
    path('ward-autocomplete/', WardAutocomplete.as_view(), name='ward-autocomplete'),
]
