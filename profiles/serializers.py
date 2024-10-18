from rest_framework import serializers
from .models import Profile
from games.models import Game


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    games_count = serializers.ReadOnlyField()

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_games_count(self, obj):
        # Assuming the Game model has a ForeignKey to the Profile's owner (User)
        return Game.objects.filter(owner=obj.owner).count()

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'name',
            'favourite_game', 'image', 'is_owner', 'games_count',
            ]