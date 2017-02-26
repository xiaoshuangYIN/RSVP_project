from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from .forms import EventForm
from .models import Event


# Create your views here.
def create_event(request):
    f = open('log_file', 'w')
    def create_group(group_name):
        new_group= Group(name=group_name)
        new_group.save()
        return new_group
    
    form_class = EventForm
    template_name = 'CreateEvent.html'
    
    if request.method == 'GET':
        form = form_class()
        return render(request, template_name, {'event_form':form})
    
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            # get the cleaned data (normalized data)
            event_name = form.cleaned_data['Event_name']
            place = form.cleaned_data['Place']
            start_time = form.cleaned_data['Start_time']
            end_time = form.cleaned_data['End_time']
            
            # create a new event and save to database
            event = Event.objects.create_event(event_name, place, start_time, end_time)
            event.save()
            
            # create 3 groups for this event
            owner_group = create_group(event_name + '_owner')
            owner_group.save()
            f.write('creating group: ' + event_name + ' now.......')
            if owner_group is not None:
                f.write('owner_group created')
            else:
                f.write('owner_group not created')

            guest_group = create_group(event_name + '_guest')
            guest_group.save()
            vendor_group = create_group(event_name + '_vendor')
            vendor_group.save()
            # add this user to the owner group of this event
            request.user.groups.add(owner_group)
            f.close()
            return redirect('manageEventsIcreated')

        else:
            return redirect('userhome')
    
def manage_events(request):
    template_name = 'manageEventIcreated.html'
    return render(request, template_name)

def answer_questions(request):
    template_name = 'ansQs.html'
    return render(request, template_name)
