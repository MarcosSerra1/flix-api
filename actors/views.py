from rest_framework import generics
from actors.models import Actors
from actors.serializers import ActorSerializer
from django.http import JsonResponse


class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer


class ActorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorSerializer

    def delete(self, *args, **kwargs):
        instance = self.get_object()
        try:
            instance.delete()
            return JsonResponse(
                {'message': 'Ator deletado com sucesso.'},
                status=204
            )
        
        except Exception as e:
            return JsonResponse(
                {'error': str(e)},
                status=500
            )
