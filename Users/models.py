# Django
from django.db import models
from django.conf import settings

# Core
from Core.models import TimeStampModel


class UserInfo(TimeStampModel):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    personal_info_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.user.name