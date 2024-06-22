from rest_framework import generics
from genres.models import Genre
from genres.serializers import GenreSerializer
from django.http import JsonResponse


class GenreCreateListView(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        try: 
            instance.delete()
            return JsonResponse(
                {'message': 'Gênero deletado com sucesso.'}, 
                status=204
            )
        
        except Exception as e: 
            return JsonResponse(
                {'error': str(e)},
                status=500
            )
