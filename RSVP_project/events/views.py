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
            # start test ---------------------------------------------
            f.write('creating group: ' + event_name + ' now.......')
            if owner_group is not None:
                f.write('owner_group created')
            else:
                f.write('owner_group not created')
            f.close()
            # end test ------------------------------------------------    
            guest_group = create_group(event_name + '_guest')
            guest_group.save()
            vendor_group = create_group(event_name + '_vendor')
            vendor_group.save()
            # add this user to the owner group of this event
            request.user.groups.add(owner_group)

            return redirect('eventIndex')

        else:
            return redirect('userhome')

    
def index(request):
    event_list = Event.objects.all()# a list of objs
    
    # begin test print-------------------
    f = open('log_file', 'w')
    if event_list is not None:
        f.write('get event_list' + '\n')
        for event in event_list:
            f.write(event.event_name + '\n')
    else:
        f.write('did not get event_list')
    f.close()    
    # end test print--------------------
    
    context = {'event_list': event_list}
    return render(request, 'event_index.html', context)

def detail(request, event_id):
    template_name = 'event_detail.html'
    # get the event details
    event_name = Event.objects.get(id=event_id).event_name
    event_place = Event.objects.get(id=event_id).place
    start_time = Event.objects.get(id=event_id).start_time
    end_time = Event.objects.get(id=event_id).end_time
    link_to_add_question = 'event/' + event_id + '/createQ/'
    context = {'event_id': event_id,
               'event_name' : event_name,
               'event_place' : event_place,
               'start_time' : start_time,
               'end_time' : end_time,
               'link_to_add_question' : link_to_add_question,}

    return render(request, template_name, context)

def answer_questions(request):
    template_name = 'ansQs.html'
    return render(request, template_name)

def createQ(request, event_id):
     template_name = 'createQ.html'
     event_name = Event.objects.get(id=event_id).event_name
     context = {'event_name': event_name}
     return render(request, template_name, context)
