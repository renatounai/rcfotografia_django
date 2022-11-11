from photos.models import User, Post
from photos.models.base import BaseModel
from django.db import models


class Comment(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        related_query_name='comment',
        null=False,
        blank=False)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        related_query_name='comment',
        null=False,
        blank=False)
    text = models.TextField(blank=True, null=False, default='', max_length=1000)

    def __str__(self):
        return f'{self.user} commented {self.post}'
