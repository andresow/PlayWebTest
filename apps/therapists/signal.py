from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Therapist


@receiver(post_save, sender=User)
def create_therapist(sender, instance, created, **kwargs):
    if created:
        Therapist.objects.create(user=instance)