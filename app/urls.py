from django.urls import path

from app.views import ChallengeListAPIView, CreateChallengeTransactionView

urlpatterns = [
    path("challenges/", ChallengeListAPIView.as_view(), name="challenge_list"),
    path(
        "challenges/create/",
        CreateChallengeTransactionView.as_view(),
        name="challenge_create",
    ),
]
