from django.db import models

from product.models import Product


class Set(models.Model):
    name_set = models.CharField(verbose_name='Set name', max_length=20, unique=True)
    name_set_uk = models.CharField(verbose_name='Назва сету', max_length=20, unique=True, blank=True, null=True)
    name_set_ru = models.CharField(verbose_name='Название сета', max_length=20, unique=True, blank=True, null=True)
    description = models.TextField(verbose_name='Description')
    description_uk = models.TextField(verbose_name='Опис', blank=True, null=True)
    description_ru = models.TextField(verbose_name='Описание', blank=True, null=True)
    photo = models.ImageField(verbose_name='Photo', upload_to='set_img', blank=True, null=True)
    slug = models.SlugField(verbose_name='Part of the link', max_length=30, unique=True)
    title = models.CharField(verbose_name='Title', max_length=30, unique=True)
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
    date_create = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_set
