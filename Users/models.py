# Django
from django.db import models
from django.conf import settings

# Core
from Core.models import TimeStampModel

# Apps
from Events.models import Event


class User(TimeStampModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    registered_events = models.ManyToManyField(Event, related_name='registered_events')
    attended_events = models.ManyToManyField(Event, related_name='attended_events')

    def __str__(self):
        return self.user