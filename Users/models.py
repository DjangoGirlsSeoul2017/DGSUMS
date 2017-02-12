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

    @property
    def registered_events(self):
        return self.user.registered_users.all()

    @property
    def attended_events(self):
        return self.user.attended_users.all()

    @property
    def event_attendance_rate(self):
        reg_events_num = len(self.registered_events)
        atnd_events_num = len(self.attended_events)
        if reg_events_num == 0:
            return float(1)
        else:
            return float(atnd_events_num / reg_events_num)