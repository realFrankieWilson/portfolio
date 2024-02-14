"""Profile models"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class UserProfile(models.Model):
    """Class for users profiles """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default='def-profile-img.jpg',upload_to='profile',
        validators=[FileExtensionValidator(['png', 'jpg'])]
        )


    def __str__(self):
        """Username string representation"""
        return self.user.username
