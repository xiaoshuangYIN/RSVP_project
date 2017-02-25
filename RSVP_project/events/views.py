from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User

# Create your views here.
def create_event(request):
    template_name = 'CreateEvent.html'
    return render(request, template_name)

def manage_events(request):
    template_name = 'manageEventIcreated.html'
    return render(request, template_name)

def answer_questions(request):
    template_name = 'ansQs.html'
    return render(request, template_name)
