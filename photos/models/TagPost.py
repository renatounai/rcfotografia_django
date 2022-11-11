from photos.models import Post, Tag
from photos.models.base import BaseModel
from django.db import models


class TagPost(BaseModel):
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name='tags',
        related_query_name='tag',
        null=False,
        blank=False)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='tags',
        related_query_name='tag',
        null=False,
        blank=False)

    def __str__(self):
        return f'{self.tag} tagged {self.post}'

    class Meta:
        unique_together = ('tag', 'post')
