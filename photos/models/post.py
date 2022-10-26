from django.contrib.auth.models import User
from django.db import models

from photos.models.base import BaseModel


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    text = models.TextField(blank=True, null=False, default='', max_length=1000)
