from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User
from .forms import EventForm
from .models import Event
# Create your views here.
def create_event(request):
    form_class = EventForm
    template_name = 'CreateEvent.html'
    
    if request.method == 'GET':
        form = form_class()
        return render(request, template_name, {'event_form':form})
    
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            # cleaned (normalized data)
            event_name = form.cleaned_data['Event_name']
            place = form.cleaned_data['Place']
            start_time = form.cleaned_data['Start_time']
            end_time = form.cleaned_data['End_time']
            
            # create a new user and save to database
            user = Event.objects.create_event(event_name, place, start_time, end_time)
            user.save()
            return redirect('manageEventsIcreated')
        #TO DO else:
        else:
            return redirect('userhome')
    
def manage_events(request):
    template_name = 'manageEventIcreated.html'
    return render(request, template_name)

def answer_questions(request):
    template_name = 'ansQs.html'
    return render(request, template_name)
