from rest_framework import generics
from movies.models import Movie
from movies.serializers import MovieSerializer
from django.http import JsonResponse


class MovieCreateListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        try: 
            instance.delete()
            return JsonResponse(
                {'message': 'Filme deletado com sucesso.'}, 
                status=204
            )
        
        except Exception as e: 
            return JsonResponse(
                {'error': str(e)},
                status=500
            )
