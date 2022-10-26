from django.contrib import admin
from django.utils.html import format_html

from photos.models.album import Album
from photos.models.photo import Photo


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'width', 'height', 'show_in_nav_bar', 'image_tag')
    list_filter = ('title', 'show_in_nav_bar',)
    search_fields = ('title',)
    ordering = ('title',)

    @staticmethod
    def image_tag(album):
        return format_html('<img src="../../../{0}" style="width: 45px;" />'.format(album.banner_image))


class PhotoAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'album')
    readonly_fields = ('width', 'height')

    @staticmethod
    def image_tag(photo):
        return format_html('<img src="../../../{0}" style="height: 100px;" />'.format(photo.image))


admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)

