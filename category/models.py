from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Category(models.Model):

    name_category = models.CharField(verbose_name='Name', max_length=30, unique=True)
    photo = models.ImageField(verbose_name='Photo', null=True, blank=True, upload_to='images')
    description = models.TextField(verbose_name='Description')
    title = models.CharField(verbose_name='Title', max_length=30)
    status = models.BooleanField(verbose_name='Status', default=True)
    date_create = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    parent_category = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    users = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name_category
