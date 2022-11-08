from django.db import models

from photos.models.base import BaseModel
from rcfotografia_django import settings


class Post(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    text = models.TextField(blank=True, null=False, default='', max_length=1000)
