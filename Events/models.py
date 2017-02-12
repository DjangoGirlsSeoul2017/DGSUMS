# Django / Python
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model

# Core
from Core.models import TimeStampModel
from Core.models import ImageModel

# Apps
from Users.models import UserInfo


class Event(TimeStampModel):
    EVENT_TYPES = (
        (1, 'DjangoGirls Seminar'),
        (2, 'Community Tutorial'),
        (3, 'Community Meetup'),
    )

    name = models.CharField(max_length=200)
    content = models.TextField()
    event_start = models.DateField()
    event_end = models.DateField()
    register_fee = models.PositiveIntegerField()
    register_start = models.DateField()
    register_end = models.DateField()
    registered_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='registered_users'
    )
    max_attend_user = models.PositiveSmallIntegerField()
    attended_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='attended_users'
    )
    event_type = models.PositiveSmallIntegerField(choices=EVENT_TYPES)

    def __str__(self):
        return self.title

    @property
    def can_register(self):
        if (self.register_start < timezone.now() < self.register_end):
            return True
        return False

    def if_user_registered(self, user_pk):
        user = get_user_model().objects.get(pk=user_pk)
        if user in self.registered_users:
            return True
        return False


class EventImage(ImageModel):
    event = models.ForeignKey(Event)


class Study(TimeStampModel):
    name = models.CharField(max_length=200)
    content = models.TextField()
    study_start = models.DateField()
    study_end = models.DateField()
    register_fee = models.PositiveIntegerField()
    register_start = models.DateField()
    register_end = models.DateField()
    registered_users = models.ManyToManyField(settings.AUTH_USER_MODEL)

    @property
    def study_weeks(self):
        return ((self.study_end - self.study_start).days / 7) + 1

    @property
    def can_register(self):
        if (self.register_start < timezone.now() < self.register_end):
            return True
        return False

    def if_user_registered(self, user_pk):
        user = get_user_model().objects.get(pk=user_pk)
        if user in self.registered_users:
            return True
        return False

    def __str__(self):
        return self.name


class StudyImage(ImageModel):
    study = models.ForeignKey(Study)


class StudyTimes(TimeStampModel):
    study = models.ForeignKey(Study)
    attended_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    times = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.study.name + ': ' + str(self.times) + '회'


class StudyTimesImage(ImageModel):
    studytimes = models.ForeignKey(StudyTimes)

