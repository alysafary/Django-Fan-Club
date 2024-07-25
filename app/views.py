# views.py
from django.contrib.auth import get_user_model
from django.db import transaction
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ChallengeTransaction
from .models.challenge import ChallengeItem
from .serializers import ChallengeItemSerializer, ChallengePostSerializer

User = get_user_model()


class ChallengeListAPIView(ListAPIView):
    serializer_class = ChallengeItemSerializer
    permission_classes = (IsAuthenticated,)
    queryset = ChallengeItem.objects.all()


class CreateChallengeTransactionView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ChallengePostSerializer

    def post(self, request):
        user = request.user
        challenge_item_ids = request.data.get("challenge_item_ids", [])

        if not challenge_item_ids:
            return Response(
                data={"message": "challenge item ids are missing"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        challenge_items = ChallengeItem.objects.prefetch_related("transactions").filter(
            id__in=challenge_item_ids
        )

        with transaction.atomic():
            for challenge_item in challenge_items:
                if challenge_item.transactions.filter(user=user).exists():
                    return Response(
                        {"message": "you can do a challenge just once"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                ChallengeTransaction.objects.create(
                    user=user, challenge_item=challenge_item
                )

        return Response(status=status.HTTP_201_CREATED)
