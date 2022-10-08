from django.contrib import admin
from .models import ParticipantEvent, QuestionAnswer, Event

admin.site.register(ParticipantEvent)
admin.site.register(QuestionAnswer)
admin.site.register(Event)