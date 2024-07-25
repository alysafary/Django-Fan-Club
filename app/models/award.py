from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Award(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class AwardTransaction(models.Model):
    award = models.ForeignKey(
        Award, on_delete=models.CASCADE, related_name="transactions"
    )
    user = models.ForeignKey(
        "app.User", on_delete=models.CASCADE, related_name="award_transactions"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.award.name
