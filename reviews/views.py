from rest_framework import generics
from reviews.models import Review
from reviews.serializers import ReviewSerializer
from django.http import JsonResponse


class ReviewCreateListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

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
