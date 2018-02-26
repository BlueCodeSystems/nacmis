from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

# Create your views here.
'''
class IndexView(generic.ListView):
    template_name = 'data_collector_app/index.html'
    context_object_name = 'test_list'

    def get_queryset(self):
        """
        testing the index
        """
        fruit_list = ['Lemons', 'Apples', 'Oranges', 'Granadillas', 'Guavas']
        return fruit_list


class StakeHolderView(generic.DetailView):
    return HttpResponse("Hello, stake holder. This is your page.")
    
class ReportView(generic.DetailView):
    return HttpResponse("Reporting form page.")

class ParticipationView(generic.DetailView):
    return HttpResponse("HIV activities organization participates in page.")

class SituationRoomView(generic.DetailView):
    return HttpResponse("Reporting form page.")
'''
def index(request):
    return HttpResponse("This is my index.")