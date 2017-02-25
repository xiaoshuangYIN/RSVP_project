from django.db import models


# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)    
    date_create = models.DateField()
    date_happen = models.DateField()
    

class Question(models.Model):
    # belongs to event
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    # normal fields
    question_text = models.CharField(max_length=200)

class Choice(models.Model):
    # belongs to questions
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # normal fields
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


    
    
