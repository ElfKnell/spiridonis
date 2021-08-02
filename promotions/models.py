from django.db import models
from product.models import Product


class Promotions(models.Model):
    name_promotions = models.CharField(verbose_name='Name', unique=True, max_length=20)
    sale = models.CharField(verbose_name='Sale', max_length=5)
    photo = models.ImageField(verbose_name='Photo', upload_to='promotions_img', blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name_promotions
