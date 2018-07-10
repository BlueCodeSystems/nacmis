from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic, View
from dal import autocomplete
from django import forms
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import District, Ward, OrganisationTarget, SupportField, SourcesOfInformation,\
    UserProfile, StakeholderDirectory
from .forms import StakeholderDirectoryModelForm, ProgramActivityModelForm, MyForm

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'data_entry/index.html'
    context_object_name = 'test_list'

    def get_queryset(self):
        """
        testing the index
        """
        fruit_list = ['Lemons', 'Apples', 'Oranges', 'Granadillas', 'Guavas']
        return fruit_list

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

class SupportFieldAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        
        #if not self.request.user.is_authenticated():
        #    return SupportField.objects.none()

        qs = SupportField.objects.all()

        if self.q:
            qs = qs.filter(area_of_support__istartswith=self.q)
        return qs

class OrganisationTargetAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        
        #if not self.request.user.is_authenticated():
        #    return OrganisationTarget.objects.none()

        qs = OrganisationTarget.objects.all()

        if self.q:
            qs = qs.filter(organisation_target_option__istartswith=self.q)
        return qs

class SourcesOfInformationAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
    
        #if not self.request.user.is_authenticated():
        #    return District.objects.none()

        qs = SourcesOfInformation.objects.all()

        if self.q:
            qs = qs.filter(source__istartswith=self.q)
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