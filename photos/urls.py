from django.urls import path
from photos.views.index import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
