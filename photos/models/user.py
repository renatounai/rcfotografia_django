from django.contrib.auth.models import AbstractUser
from django.db import models
from django_resized import ResizedImageField


class User(AbstractUser):
    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False, unique=True)
    password = models.CharField(max_length=100, blank=False, null=False)
    photo = ResizedImageField(
        size=[500, 500],
        quality=80,
        upload_to='users',
        blank=True,
        null=True)
    is_active = models.BooleanField(default=True)
    bio = models.TextField(blank=True, null=False, default='', max_length=1000)
