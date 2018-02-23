from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, welcome to the nacmis index page")

def stake_holder(request):
    return HttpResponse("Hello, stake holder. This is your page.")
    
def report(request):
    return HttpResponse("Reporting form page.")

def participation(request):
    return HttpResponse("HIV activities organization participates in page.")

def situation_room(request):
    return HttpResponse("Reporting form page.")