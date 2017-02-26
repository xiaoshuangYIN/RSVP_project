from django.contrib import admin
from .models import Event
from .models import Question
from .models import Choice

# Register your models here.
admin.site.register(Event)
admin.site.register(Question)
admin.site.register(Choice)
