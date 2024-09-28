from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from drf_api_bg.permissions import IsOwnerOrReadOnly
from .models import Rating
from .serializers import RatingSerializer


class RatingList(generics.ListCreateAPIView):
    """
    List ratings or create a rating if logged in.
    """
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Rating.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['game']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a rating, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()