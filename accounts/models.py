from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(
        upload_to="avatars/",
        blank=True,
        null=True
    )

    bio = models.TextField(
        blank=True
    )

    is_online = models.BooleanField(
        default=False
    )

    last_seen = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.username