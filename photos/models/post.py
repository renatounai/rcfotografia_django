from django.db import models

from photos.models.Tag import Tag
from photos.models.base import BaseModel
from rcfotografia_django import settings


class Post(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False)
    text = models.TextField(blank=True, null=False, default='', max_length=1000)

    def __str__(self):
        return f'{self.user} - {self.text[:25]}'

    def after_save(self):
        from photos.models.TagPost import TagPost

        # TODO - change this to a queue
        TagPost.objects.filter(post=self).delete()

        tags_in_the_current_text = [tag for tag in self.text.split() if tag.startswith('#')]
        tags = [Tag.objects.get_or_create(name=tag) for tag in tags_in_the_current_text]
        for tag in tags:
            TagPost.objects.create(tag=tag, post=self)
