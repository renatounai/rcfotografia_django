from django.db import models
from django_resized import ResizedImageField

from photos.models.base import BaseModel
from photos.models.post import Post


class Photo(BaseModel):
    image = ResizedImageField(
        size=[1024, 1024],
        quality=80,
        upload_to='photos',
        blank=True,
        null=True,
        width_field="width",
        height_field="height",)
    width = models.IntegerField(editable=False)
    height = models.IntegerField(editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'Photo {self.image.name}-{self.width}x{self.height}'

