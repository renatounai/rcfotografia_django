from django.db import models
from django_resized import ResizedImageField

from photos.models.base import BaseModel
from photos.models.post import Post


class Photo(BaseModel):
    image = ResizedImageField(
        size=[2048, 2048],
        quality=80,
        upload_to='photos',
        blank=True,
        null=True,
        width_field="width",
        height_field="height",)
    width = models.IntegerField(editable=False)
    height = models.IntegerField(editable=False)
    text = models.TextField(blank=True, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)

