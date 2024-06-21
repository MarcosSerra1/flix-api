from django.urls import path
from genres.views import genre_create_list_view


urlpatterns = [
    path('genres/', genre_create_list_view, name='genre')
]
