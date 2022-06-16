from typing import Any, Type

from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import CustomUser, UserProfile


@receiver(post_save, sender=CustomUser)
def create_profile(
    sender: Type[CustomUser],
    instance: CustomUser,
    created: bool,
    **kwargs: Any
) -> None:
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_profile(
    sender: Type[CustomUser], instance: CustomUser, **kwargs: Any
) -> None:
    instance.profile.save()
