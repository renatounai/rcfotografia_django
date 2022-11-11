from photos.models import User, Photo
from photos.models.base import BaseModel
from django.db import models


class Favorite(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        related_query_name='favorite',
        null=False,
        blank=False)
    photo = models.ForeignKey(
        Photo,
        on_delete=models.CASCADE,
        related_name='favorites',
        related_query_name='favorite',
        null=False,
        blank=False)

    def __str__(self):
        return f'{self.user} favorited {self.photo}'

    class Meta:
        unique_together = ('user', 'photo')
