from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.views import generic, View
from dal import autocomplete
from django import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.gzip import gzip_page

from django.core import serializers
from django.db.models import Count
from .models import NationalOrganisation, District, Ward, OrganisationTarget, \
    PreventionMessageList, SupportField, SupportByArea, SourcesOfInformation, \
    UserProfile, StakeholderDirectory, ProgramActivity, Province
from .forms import StakeholderDirectoryModelForm, ProgramActivityModelForm, MyForm

# Create your views here.

class SupportFieldAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        
        #if not self.request.user.is_authenticated():
        #    return SupportField.objects.none()

        qs = SupportField.objects.all()

        if self.q:
            qs = qs.filter(area_of_support__istartswith=self.q)
        return qs

class SupportByAreaAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        
        #if not self.request.user.is_authenticated():
        #    return SupportField.objects.none()

        qs = SupportByArea.objects.all()

        if self.q:
            qs = qs.filter(area_of_support2__istartswith=self.q)
        return qs

class OrganisationTargetAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        
        #if not self.request.user.is_authenticated():
        #    return OrganisationTarget.objects.none()

        qs = OrganisationTarget.objects.all()

        if self.q:
            qs = qs.filter(organisation_target_option__istartswith=self.q)
        return qs

class PreventionMessageListAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        
        #if not self.request.user.is_authenticated():
        #    return OrganisationTarget.objects.none()

        qs = PreventionMessageList.objects.all()

        if self.q:
            qs = qs.filter(prevention_message__istartswith=self.q)
        return qs

class SourcesOfInformationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
    
        #if not self.request.user.is_authenticated():
        #    return District.objects.none()

        qs = SourcesOfInformation.objects.all()

        if self.q:
            qs = qs.filter(source__istartswith=self.q)
        return qs

class NationalOrganisationAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = NationalOrganisation.objects.all()


        if self.q:
            qs = qs.filter(organisation_name__istartswith=self.q)
        return qs
        

class DistrictAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        
        qs = District.objects.all()

        #filter to only show districts allowed for the logged in user
        if not self.request.user.is_superuser:
            try:
                userProfile = UserProfile.objects.get(user=self.request.user)
            except UserProfile.DoesNotExist:
                #No userprofile set, return empty queryset
                return qs.none()
            else: 
                if self.request.user.groups.filter(name="Stakeholder"):
                    qs = qs.filter(id=userProfile.stakeholder.id)
                if self.request.user.groups.filter(name="DACA"):
                    qs = qs.filter(name=userProfile.district.name)
                if self.request.user.groups.filter(name="PACA"):
                    qs = qs.filter(name=userProfile.district.province.name)

        province = self.forwarded.get('organisation_province', None) or self.forwarded.get('province', None)

        if province:
            qs = qs.filter(province=province)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs

class WardAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
    
        #if not self.request.user.is_authenticated():
        #    return District.objects.none()

        qs = Ward.objects.all()
        district = self.forwarded.get('organisation_district', None)

        if district:
            qs = qs.filter(district=district)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs

class StakeholderAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
    
        #if not self.request.user.is_authenticated():
        #    return District.objects.none()

        qs = StakeholderDirectory.objects.all()
        national_organisation_id = self.forwarded.get('national_organisation', None)

        if national_organisation_id:
            qs = qs.filter(national_organisation__id=national_organisation_id)
        #filter to only show stakeholders in users district
        if not self.request.user.is_superuser:
            try:
                userProfile = UserProfile.objects.get(user=self.request.user)
            except UserProfile.DoesNotExist:
                #No userprofile set, return empty queryset
                return qs.none()
            else: 
                if self.request.user.groups.filter(name="DACA"):
                    qs = qs.filter(organisation_district=userProfile.district)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs

"""
if (iecmaterial == True):
    if id == 'iecmaterial_set-group':
        add class to hide/ grey out div
elif (iecmaterial2 == True):
    if id == 'iecmaterial_set-group':
        add class to hide/ grey out div
elif (teacher == True):
    if id == 'teachers_set-group':
        add class to hide/ grey out div
elif (outofschool == True):
    if id == 'outofschool_set-group':
        add class to hide/ grey out div
elif (sexworker == True):
    if id == 'sexworker_set-group':
        add class to hide/ grey out div
elif (inmate == True):
    if id == 'inmate_set-group':
        add class to hide/ grey out div
elif (personswithdisability == True):
    if id == 'personswithdisabilty_set-group':
        add class to hide/ grey out div
elif (mobileworker == True):
    if id == 'mobileworker_set-group':
        add class to hide/ grey out div
elif (mobilepopulation == True):
    if id == 'mobilepopulation_set-group':
        add class to hide/ grey out div
elif (menwithmen == True):
    if id == 'menwithmen_set-group':
        add class to hide/ grey out div
elif (transgenderindividual == True):
    if id == 'transgenderindividual_set-group':
        add class to hide/ grey out div
elif (peoplewhoinjectdrug == True):
    if id == 'peoplewhoinjectdrug_set-group':
        add class to hide/ grey out div
elif (condomprogramming == True):
    if id == 'condomprogramming_set-group':
        add class to hide/ grey out div
elif (condomprogramming2 == True):
    if id == 'condomprogramming2_set-group':
        add class to hide/ grey out div
elif (reportedcase == True):
    if id == 'reportedcase_set-group':
        add class to hide/ grey out div
elif (experiencedphysicalviolence == True):
    if id == 'experiencedphysicalviolence_set-group':
        add class to hide/ grey out div
elif (experiencedsexualviolence == True):
    if id == 'experiencedsexualviolence_set-group':
        add class to hide/ grey out div
elif (postexposureprophylaxis == True):
    if id == 'postexposureprophylaxis_set-group':
        add class to hide/ grey out div
elif (preexposureprophylaxis == True):
    if id == 'preexposureprophylaxis_set-group':
        add class to hide/ grey out div
elif (synergydevelopmentsector == True):
    if id == 'synergydevelopmentsector_set-group':
        add class to hide/ grey out div
elif (supportgroupsetup == True):
    if id == 'supportgroupsetup_set-group':
        add class to hide/ grey out div
elif (individualcurrentlyenrolled == True):
    if id == 'individualcurrentlyenrolled_set-group':
        add class to hide/ grey out div
elif (vulnerablepeople == True):
    if id == 'vulnerablepeople_set-group':
        add class to hide/ grey out div
elif (supportandcare == True):
    if id == 'supportandcare_set-group':
        add class to hide/ grey out div
"""

def comingSoonView(request):
    #nocontext = null
    return render(request, 'data_entry/coming_soon.html')

# ------ Landing or Home page for the front end ------ #
class HomeView(View):
    form_class = MyForm
    #form_class = None
    initial = {'key': 'value'}
    template_name = 'data_entry/nacmis_metronic/index.html'

    # GET logic
    def get(self, request, *args, **kwargs):
        if self.form_class:
            form = self.form_class(initial=self.initial)
        else:
            form = forms.Form()
        return render(request, self.template_name, {'form': form})

    # POST logic
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

class ResourcesView(View):
    form_class = MyForm
    #form_class = None
    initial = {'key': 'value'}
    template_name = 'data_entry/nacmis_metronic/resources.html'

    # GET logic
    def get(self, request, *args, **kwargs):
        if self.form_class:
            form = self.form_class(initial=self.initial)
        else:
            form = forms.Form()
        return render(request, self.template_name, {'form': form})
    
    # POST logic
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

@method_decorator(login_required, name='dispatch')
class StakeholdersView(View):
    form_class = None
    initial = {'key': 'value'}
    template_name = 'data_entry/nacmis_metronic/stakeholder.html'

    # GET logic
    def get(self, request, *args, **kwargs):
        if self.form_class:
            form = self.form_class(initial=self.initial)
        else:
            form = forms.Form()
        
        userProfile = None
        if request.user.is_authenticated:
            try:
                userProfile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                userProfile = None
        return render(request, self.template_name, {'form': form, 'userProfile':userProfile})

    # POST logic
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

@method_decorator(login_required, name='dispatch')
class ActivityReportsView(View):
    form_class = None
    initial = {'key': 'value'}
    template_name = 'data_entry/nacmis_metronic/activityreport.html'

    # GET logic
    def get(self, request, *args, **kwargs):
        if self.form_class:
            form = self.form_class(initial=self.initial)
        else:
            form = forms.Form()
        userProfile = None
        if request.user.is_authenticated:
            try:
                userProfile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                userProfile = None
        return render(request, self.template_name, {'form': form, 'userProfile':userProfile})

    # POST logic
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

@method_decorator(login_required, name='dispatch')
class KeyPopulationsView(View):
    form_class = None
    initial = {'key': 'value'}
    template_name = 'data_entry/nacmis_metronic/keypopulations.html'

    # GET logic
    def get(self, request, *args, **kwargs):
        if self.form_class:
            form = self.form_class(initial=self.initial)
        else:
            form = forms.Form()
        userProfile = None
        if request.user.is_authenticated:
            try:
                userProfile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                userProfile = None
        return render(request, self.template_name, {'form': form})

    # POST logic
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

@method_decorator(login_required, name='dispatch')
class InternalMonitoringView(View):
    form_class = None
    initial = {'key': 'value'}
    template_name = 'data_entry/nacmis_metronic/internalmonitoring.html'

    # GET logic
    def get(self, request, *args, **kwargs):
        if self.form_class:
            form = self.form_class(initial=self.initial)
        else:
            form = forms.Form()
        userProfile = None
        if request.user.is_authenticated:
            try:
                userProfile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                userProfile = None
        return render(request, self.template_name, {'form': form})

    # POST logic
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

@method_decorator(login_required, name='dispatch')
class PACADashboardView(View):
    form_class = None
    initial = {'key': 'value'}
    template_name = 'data_entry/nacmis_metronic/pacadashboard.html'

    # GET logic
    def get(self, request, *args, **kwargs):
        if self.form_class:
            form = self.form_class(initial=self.initial)
        else:
            form = forms.Form()
        userProfile = None
        if request.user.is_authenticated:
            try:
                userProfile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                userProfile = None
        return render(request, self.template_name, {'form': form})

    # POST logic
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

@method_decorator(login_required, name='dispatch')
class PITMEODashboardView(View):
    form_class = None
    initial = {'key': 'value'}
    template_name = 'data_entry/nacmis_metronic/pitmeodashboard.html'

    # GET logic
    def get(self, request, *args, **kwargs):
        if self.form_class:
            form = self.form_class(initial=self.initial)
        else:
            form = forms.Form()
        userProfile = None
        if request.user.is_authenticated:
            try:
                userProfile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                userProfile = None
        return render(request, self.template_name, {'form': form})

    # POST logic
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

@method_decorator(login_required, name='dispatch')
class DACADashboardView(View):
    form_class = None
    initial = {'key': 'value'}
    template_name = 'data_entry/nacmis_metronic/dacadashboard.html'

    # GET logic
    def get(self, request, *args, **kwargs):
        if self.form_class:
            form = self.form_class(initial=self.initial)
        else:
            form = forms.Form()
        userProfile = None
        if request.user.is_authenticated:
            try:
                userProfile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                userProfile = None
        return render(request, self.template_name, {'form': form})

    # POST logic
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

class HelpView(View):
    form_class = None
    initial = {'key': 'value'}
    template_name = 'data_entry/nacmis_metronic/help.html'

    # GET logic
    def get(self, request, *args, **kwargs):
        if self.form_class:
            form = self.form_class(initial=self.initial)
        else:
            form = forms.Form()
        userProfile = None
        if request.user.is_authenticated:
            try:
                userProfile = UserProfile.objects.get(user=request.user)
            except UserProfile.DoesNotExist:
                userProfile = None
        return render(request, self.template_name, {'form': form})

class UReportView(View):
    form_class = MyForm
    #form_class = None
    initial = {'key': 'value'}
    template_name = 'data_entry/nacmis_metronic/ureportdashboard.html'

    # GET logic
    def get(self, request, *args, **kwargs):
        if self.form_class:
            form = self.form_class(initial=self.initial)
        else:
            form = forms.Form()
        return render(request, self.template_name, {'form': form})
    
    # POST logic
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

# test classes

class IndexView(generic.ListView):
    template_name = 'data_entry/index.html'
    context_object_name = 'test_list'

class Login(generic.DetailView):
    template_name = 'data_entry/login.html'
    def get_queryset(self):
        return

def get_nameinmodel(request):
    if request.method == 'POST':
        form = StakeholderDirectoryModelForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            return redirect('data_entry/next_page.html')
        else:
            form = StakeholderDirectoryModelForm()
    else:
        form = StakeholderDirectoryModelForm()
    
    return render(request, 'data_entry/index.html', {'form': form})

def myform_test(request):
    formsample = MyForm()
    return render(request, 'data_entry/index.html', {'the_insert': formsample} )

@method_decorator(login_required, name='dispatch')
class MapDashboardView(generic.TemplateView):
    template_name = 'data_entry/nacmis_metronic/map.html'


@method_decorator(gzip_page, name='dispatch')
@method_decorator(login_required, name='dispatch')
class MapDashboardJSON(View):
    def get(self, context, *response_kwargs):
        data = {}
        data["districtData"] = {}
        data["provinceData"] = {}
        data["wardData"] = {}
        for province in Province.objects.all():
            programActivities = ProgramActivity.objects.filter(
                ward__district__province=province).exclude(
                    areas_of_support2__support_given_at_area=None).values_list(
                        "areas_of_support2__support_given_at_area").annotate(
                            number=Count("areas_of_support2__support_given_at_area"))
            data["provinceData"][province.name] = []
            for activity in programActivities:
                data["provinceData"][province.name].append({"service":activity[0], "number": activity[1]})
        for district in District.objects.all():
            programActivities = ProgramActivity.objects.filter(
                ward__district=district).exclude(
                    areas_of_support2__support_given_at_area=None).values_list(
                        "areas_of_support2__support_given_at_area").annotate(
                            number=Count("areas_of_support2__support_given_at_area"))
            data["districtData"][district.name] = []
            for activity in programActivities:
                data["districtData"][district.name].append({"service":activity[0], "number": activity[1]})
        for ward in Ward.objects.all():
            programActivities = ProgramActivity.objects.filter(
                ward=ward).exclude(
                    areas_of_support2__support_given_at_area=None).values_list(
                        "areas_of_support2__support_given_at_area").annotate(
                            number=Count("areas_of_support2__support_given_at_area"))
            data["wardData"][ward.name] = []
            for activity in programActivities:
                data["wardData"][ward.name].append({"service":activity[0], "number": activity[1]})
        jsdata = data
        return JsonResponse(jsdata, safe=False)


