from django.db import models


class TimeStampModel(models.Model):
    class Meta:
        abstract=True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ImageModel(TimeStampModel):
    class Meta:
        abstract=True

    image = models.ImageField(upload_to='%Y/%m/%d/')

    def __str__(self):
        return self.image.name
