from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify

User = get_user_model()


class News(models.Model):
    post = models.CharField(verbose_name="Post", max_length=50, unique=True)
    uk_post = models.CharField(verbose_name="Новини", max_length=50, unique=True, null=True)
    ru_post = models.CharField(verbose_name="Новости", max_length=50, unique=True, null=True)
    title = models.CharField(verbose_name='Title', max_length=50)
    part_link = models.SlugField(verbose_name='Part of the link', max_length=30, unique=True)
    photo = models.ImageField(verbose_name='Photo', blank=True, null=True, upload_to='img_news')
    date_create = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name='Text')
    uk_text = models.TextField(verbose_name='Текст', null=True)
    ru_text = models.TextField(verbose_name='Текст', null=True)

    users = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.post
