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
from data_entry import views
from data_entry.views import SupportFieldAutocomplete, SupportByAreaAutocomplete, SourcesOfInformationAutocomplete, \
    NationalOrganisationAutocomplete, DistrictAutocomplete, WardAutocomplete, OrganisationTargetAutocomplete, \
    PreventionMessageListAutocomplete, comingSoonView, StakeholderAutocomplete, MapDashboardJSON

urlpatterns = [
    path('admin/', admin.site.urls, name='admin-landing'),
    path('data_entry/', include('data_entry.data_urls')),

    #urls for front end
    path('', views.HomeView.as_view(), name='home-view'),
    path('stakeholders/', views.StakeholdersView.as_view(), name='stakeholders-view'),
    path('activity-reports/', views.ActivityReportsView.as_view(), name='activity-reports-view'),
    path('key-populations/', views.KeyPopulationsView.as_view(), name='key-populations-view'),
    path('internal-monitoring', views.InternalMonitoringView.as_view(), name='internal-monitoring-view'),
    path('paca-dashboard', views.PACADashboardView.as_view(), name='paca-dashboard-view'),
    path('pitmeo-dashboard', views.PITMEODashboardView.as_view(), name='pitmeo-dashboard-view'),
    path('daca-dashboard', views.DACADashboardView.as_view(), name='daca-dashboard-view'),
    path('ureport-dashboard', views.UReportDashboardView.as_view(), name='ureport-dashboard-view'),
    path('help/', views.HelpView.as_view(), name='help-view'),
    path('resources/', views.ResourcesView.as_view(), name='resources-view'),

    # urls for autocompletes implementation
    path('supportfield-autocomplete/', SupportFieldAutocomplete.as_view(), 
        name='supportfield-autocomplete'),
    path('supportbyarea-autocomplete/', SupportByAreaAutocomplete.as_view(), 
        name='supportbyarea-autocomplete'),
    path('supportofinformation-autocomplete/', SourcesOfInformationAutocomplete.as_view(), 
        name='supportofinformation-autocomplete'),
    path('organisationtarget-autocomplete/', OrganisationTargetAutocomplete.as_view(), 
        name='organisationtarget-autocomplete'),
    path('preventionmessagelist-autocomplete/', PreventionMessageListAutocomplete.as_view(), 
        name='preventionmessagelist-autocomplete'),
    path('district-autocomplete/', DistrictAutocomplete.as_view(), name='district-autocomplete'),
    path('ward-autocomplete/', WardAutocomplete.as_view(), name='ward-autocomplete'),
    path('stakeholder-autocomplete/', StakeholderAutocomplete.as_view(), name='stakeholder-autocomplete'),
    path('national-organisation-autocomplete/', NationalOrganisationAutocomplete.as_view(), name='national-organisation-autocomplete'),
    path('map-json/', MapDashboardJSON.as_view(), name='map-json'),

    # urls for password reset implementation
    path('', include('django.contrib.auth.urls')),
]
