from django.db import models
from django_resized import ResizedImageField

from photos.models.base import BaseModel


class Album(BaseModel):
    title = models.CharField(max_length=30)
    show_in_nav_bar = models.BooleanField(default=True)
    banner_image = ResizedImageField(
        size=[600, 600],
        quality=75,
        upload_to='album_banners',
        blank=True,
        null=True,
        width_field="width",
        height_field="height",
    )
    width = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return self.title
