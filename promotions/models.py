from django.db import models
from product.models import Product


class Promotions(models.Model):
    name_promotions = models.CharField(verbose_name='Name', unique=True, max_length=20)
    name_promotions_uk = models.CharField(verbose_name='Назва', unique=True, max_length=20, blank=True, null=True)
    name_promotions_ru = models.CharField(verbose_name='Название', unique=True, max_length=20, blank=True, null=True)
    sale = models.CharField(verbose_name='Sale', max_length=5)
    slug = models.SlugField(verbose_name='Part of the link', max_length=30, unique=True)
    title = models.CharField(verbose_name='Title', max_length=30, unique=True)
    photo = models.ImageField(verbose_name='Photo', upload_to='promotions_img', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name_promotions
