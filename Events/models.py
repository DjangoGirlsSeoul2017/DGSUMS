# Django / Python
from django.db import models
from django.utils import timezone

# Core
from Core.models import TimeStampModel

# Apps
from Users.models import User


class Event(TimeStampModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True)

    register_until = models.DateTimeField()

    registered_users = models.ManyToManyField(User, related_name='registered_users')
    attended_users = models.ManyToManyField(User, related_name='attended_users')

    def __str__(self):
        return self.title

    @property
    def can_register(self):
        if timezone.now() < self.registered_events:
            return True
        return False

    def is_user_registered(self, user_pk):
        user = User.objects.get(pk=user_pk)
        if user in self.registered_users:
            return True
        return False
