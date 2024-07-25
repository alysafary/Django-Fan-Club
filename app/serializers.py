# serializers.py
from rest_framework import serializers

from app.models.challenge import ChallengeItem


class ChallengeItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChallengeItem
        fields = (
            "id",
            "title",
            "description",
        )


class ChallengePostSerializer(serializers.Serializer):
    challenge_item_ids = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )
