from django.shortcuts import render
from django.views.generic import TemplateView

from photos.models import Photo


class IndexView(TemplateView):
    template_name = 'photos/index.html'

    def get(self, request):
        photos = Photo.objects.all()
        padding = 3 - len(photos) % 3

        photos_padding = []
        if padding < 3:
            for i in range(padding):
                photos_padding.append(Photo())

        context = {'photos': photos, 'photos_padding': photos_padding}
        return render(request, self.template_name, context)
