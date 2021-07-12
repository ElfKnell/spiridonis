from django.db import models
from product.models import Product


class RatingStar(models.Model):
    value = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        ordering = ['-value']


class Rating(models.Model):
    ip = models.CharField(verbose_name='IP address', max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rating')

    def __str__(self):
        return f'{self.star} - {self.product}'
