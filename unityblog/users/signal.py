"""
    Creates a new UserProfile object whenever a new User object
    is created in the Django app.
"""
from django.contrib.auth.models import User
from .models import UserProfile
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_profile(sender, created, instance, *args, **kwargs):
    """
        @receiver decorator specifies that create_profile fuction
        should be called when a post_save signal is sent by the
        User model.

        args:
            sender: The model class that sends the signal
            created: This is a boolean value indicating whether a new
                     instance was created or an existing instace was updated.
            instance: The instance of the model that was just saved.
            args
            kwargs
    """
    if created:
        UserProfile.objects.create(user=instance)



