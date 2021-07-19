from django.db import models

from product.models import Product


class Set(models.Model):
    name_set = models.CharField(verbose_name='Set name', max_length=20, unique=True)
    description = models.TextField(verbose_name='Description')
    photo = models.CharField(verbose_name='Photo', max_length=120)
    main_product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='main')
    product_1 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='first')
    product_2 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='second', blank=True, null=True)
    product_3 = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='third', blank=True, null=True)
    price = models.DecimalField(verbose_name='Price', blank=True, null=True, decimal_places=2, max_digits=10)
    opt_price = models.DecimalField(verbose_name='Opt price', blank=True, null=True,
                                    decimal_places=2, max_digits=10)
    small_opt_price = models.DecimalField(verbose_name='Small opt price', decimal_places=2, max_digits=10,
                                          blank=True, null=True)
    sale_price = models.DecimalField(verbose_name='Sale price', blank=True,
                                     null=True, decimal_places=2, max_digits=10)
    drop_price = models.DecimalField(verbose_name='Sale price', blank=True,
                                     null=True, decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name_set
