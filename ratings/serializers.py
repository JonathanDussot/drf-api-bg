from django.db import IntegrityError
from rest_framework import serializers
from .models import Rating

class RatingSerializer(serializers.ModelSerializer):
    """
    Serializer for the ratings model.
    """
    
    owner = serializers.ReadOnlyField(source='owner.username')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    
    class Meta:
        model = Rating
        fields = ['id', 'owner', 'profile_image', 'rating', 'game', 'created_at']
        

    def validate(self, data):
        """
        Ensure that the user has not already rated the game.
        """
        user = self.context['request'].user
        game = data['game']
        
        if self.instance is None and Rating.objects.filter(owner=user, game=game).exists():
            raise serializers.ValidationError('You have already rated this game.')
        
        return data
        
        
    def create(self, validated_data):
        """
        Validation to determine is possible duplicate of rating
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})