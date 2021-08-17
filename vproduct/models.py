from django.db import models


STATUS_CHOICE = [
    (0, 'is available'),
    (1, 'not available'),
    (2, 'in order')
]


class VProduct(models.Model):
    article = models.CharField(verbose_name='Article', max_length=30)
    price = models.DecimalField(verbose_name='Price', blank=True, null=True, decimal_places=2, max_digits=10)
    opt_price = models.DecimalField(verbose_name='Opt price', blank=True, null=True,
                                    decimal_places=2, max_digits=10)
    small_opt_price = models.DecimalField(verbose_name='Small opt price', decimal_places=2, max_digits=10,
                                          blank=True, null=True)
    drop_price = models.DecimalField(verbose_name='Dropshipper price', decimal_places=2, max_digits=10,
                                     blank=True, null=True)
    sale_price = models.DecimalField(verbose_name='Sale price', blank=True,
                                     null=True, decimal_places=2, max_digits=10)
    weight = models.FloatField(verbose_name='Weight', blank=True, null=True)
    status = models.IntegerField(verbose_name='Status', default=0, choices=STATUS_CHOICE)

    def __str__(self):
        return self.article
