from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, Group, Permission

# Create your models here.
class EventManager(models.Manager):
    def create_event(self, eventname, place, starttime, endtime):
        event = self.create(event_name=eventname, 
                            place=place,
                            start_time=starttime,
                            end_time=endtime)
        return event

class Event(models.Model):
    event_name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)    
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    objects = EventManager()
    def __str__(self):
        return self.event_name


class Question(models.Model):
    # belongs to event
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    # normal fields
    question_text = models.CharField(max_length=200)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # belongs to questions
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # normal fields
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

    
    
