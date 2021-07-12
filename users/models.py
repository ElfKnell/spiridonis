from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models


ROLE_CHOICES = (
    (1, 'manager'),
    (2, 'editor'),
    (3, 'customer'),
    (4, 'wholesaler'),
    (5, 'retail wholesaler')
)


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=10, unique=True)
    role = models.IntegerField(default=3, choices=ROLE_CHOICES, null=True)
    company = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(
        validators=[validators.validate_email],
        unique=True,
        blank=False
    )
    # Свойство `USERNAME_FIELD` сообщает нам, какое поле мы будем использовать для входа.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone', 'first_name', 'last_name', 'role', 'company']

