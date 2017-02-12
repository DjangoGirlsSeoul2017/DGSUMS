# Django / Python
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model

# Core
from Core.models import TimeStampModel

# Apps
from Users.models import UserInfo


class Event(TimeStampModel):
    name = models.CharField(max_length=200)
    content = models.TextField()
    event_start = models.DateField()
    event_end = models.DateField()
    register_fee = models.PositiveIntegerField()
    register_start = models.DateField()
    register_until = models.DateField()
    registered_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='registered_users'
    )
    max_attend_user = models.PositiveSmallIntegerField()
    attended_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='attended_users'
    )

    def __str__(self):
        return self.title

    @property
    def can_register(self):
        if timezone.now() < self.registered_events:
            return True
        return False

    def is_user_registered(self, user_pk):
        user = get_user_model().objects.get(pk=user_pk)
        if user in self.registered_users:
            return True
        return False
