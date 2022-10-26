from django.db import models
from django_resized import ResizedImageField

from photos.models.base import BaseModel


class Photo(BaseModel):
    image = ResizedImageField(
        size=[2048, 2048],
        quality=80,
        upload_to='photos',
        blank=True,
        null=True,
        width_field="width",
        height_field="height",)
    album = models.ForeignKey('Album', on_delete=models.CASCADE, related_name='photos')
    width = models.IntegerField(editable=False)
    height = models.IntegerField(editable=False)
