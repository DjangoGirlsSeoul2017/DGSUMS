# Django
from django.db import models
from django.conf import settings

# Core
from Core.models import TimeStampModel


class User(TimeStampModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.user