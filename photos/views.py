from django.http import HttpResponse
from django.shortcuts import render


# TODO - Alterar para usar Class Based Views
# TODO - Passar a colocar cada view em um arquivo separado
def index(request):
    return render(request, "photos/index.html")

