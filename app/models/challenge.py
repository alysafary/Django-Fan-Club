from django.contrib.auth import get_user_model
from django.db import models

from app.models import Award

# Create your models here.

User = get_user_model()


class Challenge(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    point = models.IntegerField()
    award = models.ForeignKey(
        Award, on_delete=models.CASCADE, related_name="challenges"
    )

    def __str__(self):
        return self.title


class ChallengeItem(models.Model):
    challenge = models.ForeignKey(
        Challenge, on_delete=models.CASCADE, related_name="items"
    )
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class ChallengeTransaction(models.Model):
    challenge_item = models.ForeignKey(
        ChallengeItem, on_delete=models.CASCADE, related_name="transactions"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="challenge_transactions"
    )
