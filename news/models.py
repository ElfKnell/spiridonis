from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class News(models.Model):
    post = models.CharField(verbose_name="Post", max_length=50, unique=True)
    title = models.CharField(verbose_name='Title', max_length=50)
    photo = models.ImageField(verbose_name='Photo', blank=True, null=True, upload_to='img_news')
    date_create = models.DateTimeField(auto_now_add=True)
    text = models.TextField(verbose_name='Text')

    users = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.post
