from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from dal import autocomplete

from .models import District, Ward, OrganisationTarget, SupportField
from .forms import StakeholderDirectoryModelForm, ProgramActivityModelForm

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

def add_clean_model(request):
    if request.method == 'POST':
        form = StakeholderDirectoryModelForm(request.POST)
        if form.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
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
        # Don't forget to filter out results depending on the visitor !
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
            qs = qs.filter(organization_target_option__istartswith=self.q)
        return qs

class DistrictAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        
        #if not self.request.user.is_authenticated():
        #    return District.objects.none()

        qs = District.objects.all()

        province = self.forwarded.get('organisation_province', None)
        print(province)

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
