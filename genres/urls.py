from django.urls import path
from genres.views import GenreCreateListView, genre_detail_view


urlpatterns = [
    path('genres/', GenreCreateListView.as_view(), name='genre'),
    path('genres/<int:pk>/', genre_detail_view, name='genre-detail-view'),
]
