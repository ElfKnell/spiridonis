from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Manufacturer(models.Model):

    name_manufacturer = models.CharField(verbose_name='Name', max_length=30, unique=True)
    description = models.TextField(verbose_name='Description', blank=True, null=True)

    users = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name_manufacturer
