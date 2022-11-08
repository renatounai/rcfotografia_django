from django.shortcuts import render

from photos.models import Photo


# TODO - Alterar para usar Class Based Views
# TODO - Passar a colocar cada view em um arquivo separado
def index(request):
    photos = Photo.objects.all()
    padding = 3 - len(photos) % 3

    photos_padding = []
    if padding < 3:
        for i in range(padding):
            photos_padding.append(Photo())

    context = {'photos': photos, 'photos_padding': photos_padding}
    return render(request, "photos/index.html", context)
