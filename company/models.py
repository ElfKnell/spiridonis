from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Company(models.Model):
    name_company = models.CharField(verbose_name='Name company', max_length=20, unique=True)
    description = models.TextField(verbose_name='Description', null=True)
    logo = models.ImageField(verbose_name='Logo', blank=True, null=True, upload_to='logo')
    phone = models.CharField(verbose_name='Phone', max_length=13, unique=True)
    email = models.EmailField(verbose_name='Email')
    address = models.CharField(verbose_name='Address', null=True, max_length=150)
    operating_mode = models.CharField(verbose_name='Operating mode', max_length=120, null=True)

    users = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name_company
