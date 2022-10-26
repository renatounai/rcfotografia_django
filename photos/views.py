from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# a view for the index.html page
def index(request):
    return render(request, "photos/index.html")


def private(request):
    return render(request, "photos/private.html")
