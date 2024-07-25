from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.models import AwardTransaction, User
from app.models.challenge import ChallengeTransaction, Challenge


@receiver(post_save, sender=ChallengeTransaction)
def create_award_transaction(sender, instance, created, **kwargs):
    if not created:
        return

    with transaction.atomic():
        locked_user: User = User.objects.select_for_update().get(pk=instance.user.pk)
        challenge = Challenge.objects.prefetch_related("items").get(
            pk=instance.challenge_item.challenge.id
        )
        user_done_challenge_items = ChallengeTransaction.objects.filter(
            user=locked_user, challenge_item__in=challenge.items.all()
        )
        if user_done_challenge_items.count() == challenge.items.count():
            AwardTransaction.objects.create(user=locked_user, award=challenge.award)
            locked_user.point_earned += challenge.point
            locked_user.save()
