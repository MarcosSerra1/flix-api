from django.urls import path
from genres.views import genre_view


urlpatterns = [
    path('genres/', genre_view, name='genre-list')
]
