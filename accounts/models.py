from django.db import models
from users.models import CustomUser


ROLE_CHOICES = (
    (1, 'customer'),
    (2, 'wholesaler'),
    (3, 'retail wholesaler')
)


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="profile")
    description = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
    is_organizer = models.BooleanField(default=False)
    role = models.IntegerField(default=1, choices=ROLE_CHOICES)

    def __str__(self):
        return self.user.username

