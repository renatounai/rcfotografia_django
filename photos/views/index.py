from django.shortcuts import render
from django.views.generic import TemplateView

from photos.models import Photo


class IndexView(TemplateView):
    template_name = 'photos/index.html'

    def get(self, request):
        photos = Photo.objects.all()
        padding = 3 - len(photos) % 3
        if padding == 3:
            padding = 0

        context = {
            'photos': photos,
            'padding': range(padding)
        }

        return render(request, self.template_name, context)
