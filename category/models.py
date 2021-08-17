from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Category(models.Model):

    name_category = models.CharField(verbose_name='Name', max_length=30, unique=True)
    uk_name_category = models.CharField(verbose_name='Назва', max_length=30, unique=True, blank=True, null=True)
    ru_name_category = models.CharField(verbose_name='Назва', max_length=30, unique=True, blank=True, null=True)
    photo = models.ImageField(verbose_name='Photo', null=True, blank=True, upload_to='images')
    description = models.TextField(verbose_name='Description')
    uk_description = models.TextField(verbose_name='Опис', blank=True, null=True)
    ru_description = models.TextField(verbose_name='Опис', blank=True, null=True)
    title = models.CharField(verbose_name='Title', max_length=30)
    slug = models.SlugField(verbose_name='Part of the link', max_length=30, unique=True)
    status = models.BooleanField(verbose_name='Status', default=True)
    date_create = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    parent_category = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL)
    users = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name_category}-{self.uk_name_category}-{self.ru_name_category}"
