from rest_framework import serializers
from django.db.models import Avg
from games.models import Game
from likes.models import Like
from ratings.models import Rating


class GameSerializer(serializers.ModelSerializer):
    """
    Serializer for Game model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    likes_count = serializers.ReadOnlyField()
    reviews_count = serializers.ReadOnlyField()
    rating_count = serializers.SerializerMethodField()
    average_rating = serializers.SerializerMethodField()

    def validate_image(self, value):
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError('Image size larger than 2MB!')
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px!'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px!'
            )
        return value

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, game=obj
            ).first()
            return like.id if like else None
        return None

    def get_rating_count(self, obj):
        return Rating.objects.filter(game=obj).count()

    def get_average_rating(self, obj):
        ratings = Rating.objects.filter(game=obj)
        if ratings.exists():
            average = ratings.aggregate(Avg('rating'))['rating__avg']
            return round(average, 1)
        return None

    class Meta:
        model = Game
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'title', 'description',
            'designer', 'artist', 'publisher',
            'min_players', 'max_players', 'solo_play',
            'image', 'genre_filter',
            'like_id', 'likes_count',
            'updated_at', 'created_at', 'reviews_count',
            'rating_count', 'average_rating',
        ]
