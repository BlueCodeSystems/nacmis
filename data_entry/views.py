from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic

from .forms import StakeholderDirectoryModelForm, MyForm

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
