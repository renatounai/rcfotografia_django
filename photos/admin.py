from django.contrib import admin
from django.utils.html import format_html

from photos.models import Post
from photos.models.photo import Photo


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image_tag',)
    readonly_fields = ('width', 'height')

    @staticmethod
    def image_tag(photo):
        return format_html('<img src="../../../{0}" style="height: 100px;" />'.format(photo.image))


admin.site.register(Photo, PhotoAdmin)
admin.site.register(Post)

