from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from dal import autocomplete

from .models import District, OrganizationTarget, SupportField
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

'''
class StakeHolderView(generic.DetailView):
    return HttpResponse("Hello, stake holder. This is your page.")
    
class ReportView(generic.DetailView):
    return HttpResponse("Reporting form page.")

class ParticipationView(generic.DetailView):
    return HttpResponse("HIV activities organization participates in page.")

class SituationRoomView(generic.DetailView):
    return HttpResponse("Reporting form page.")

'''
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

class OrganizationTargetAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        #if not self.request.user.is_authenticated():
        #    return OrganizationTarget.objects.none()

        qs = OrganizationTarget.objects.all()

        if self.q:
            qs = qs.filter(organization_target_option__istartswith=self.q)
        return qs

class DistrictAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        #if not self.request.user.is_authenticated():
        #    return District.objects.none()

        qs = District.objects.all()   # Why we need a district class here

        province = self.forwarded.get('province', None)

        if province:
            qs = qs.filter(province=province)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs
