from rest_framework.serializers import ModelSerializer
from .models import Tweet

class TweetSerializer(ModelSerializer):
    """Tweet model serializer"""
    class Meta:
        model = Tweet
        fields = '__all__'
        