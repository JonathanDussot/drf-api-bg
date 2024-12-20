from django.db.models import Count, Avg
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api_bg.permissions import IsOwnerOrReadOnly
from .models import Game
from .serializers import GameSerializer


class GameList(generics.ListCreateAPIView):
    """
    List games or create a game if logged in
    The perform_create method associates the game with the logged in user.
    """
    serializer_class = GameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Game.objects.annotate(
        likes_count=Count('likes', distinct=True),
        reviews_count=Count('review', distinct=True),
        average_rating=Avg('ratings__rating'),
        rating_count=Count('ratings', distinct=True)
    ).order_by('-created_at')
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = [
        'likes__owner__profile',
        'owner__profile',
    ]
    search_fields = [
        'owner__username',
        'title',
    ]
    ordering_fields = [
        'likes_count',
        'reviews_count',
        'rating_count',
        'average_rating',
        'likes__created_at',
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a game and edit or delete it if you own it.
    """
    serializer_class = GameSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Game.objects.annotate(
        likes_count=Count('likes', distinct=True),
        reviews_count=Count('review', distinct=True),
        average_rating=Avg('ratings__rating'),
        rating_count=Count('ratings', distinct=True)
    ).order_by('-created_at')
