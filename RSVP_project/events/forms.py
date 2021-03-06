from django.contrib.auth.models import User as User_Model
from django import forms


class EventForm(forms.Form):
    Event_name = forms.CharField(label = 'Event name', max_length=100)
    Place = forms.CharField(label = 'Place', max_length=100)
    Start_time = forms.DateTimeField(label = 'Start time', widget=forms.widgets.DateTimeInput(format=["%Y-%m-%d %H:%M:%S"], attrs={'placeholder':'yyyy-mm-dd --:--:--'}))
    End_time = forms.DateTimeField(label = 'End time', widget=forms.widgets.DateTimeInput(format=["%Y-%m-%d %H:%M:%S"], attrs={'placeholder':'yyyy-mm-dd --:--:--'}))

