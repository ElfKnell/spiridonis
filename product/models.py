from django import forms
from django.db import models
from django.contrib.auth import get_user_model

from category.models import Category
from manufacturer.models import Manufacturer


User = get_user_model()


SEX_CHOICES = [
    (0, 'children'),
    (1, 'man'),
    (2, 'woman')
]
STATUS_CHOICE = [
    (0, 'is available'),
    (1, 'not available'),
    (2, 'in order')
]


class Product(models.Model):

    name_product = models.CharField(verbose_name='Name', unique=True, max_length=30)
    title = models.CharField(verbose_name='Title', max_length=30, unique=True)
    model = models.CharField(verbose_name='Model', max_length=30, unique=True)
    article = models.CharField(verbose_name='Article', max_length=30, unique=True)
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    meta_description = models.CharField(verbose_name='Meta-description', max_length=120,
                                        blank=True, null=True)
    photo = models.CharField(verbose_name='Photo', blank=True, null=True, max_length=120)
    price = models.DecimalField(verbose_name='Price', blank=True, null=True, decimal_places=2, max_digits=10)
    opt_price = models.DecimalField(verbose_name='Opt price', blank=True, null=True,
                                    decimal_places=2, max_digits=10)
    small_opt_price = models.DecimalField(verbose_name='Small opt price', decimal_places=2, max_digits=10,
                                          blank=True, null=True)
    sale_price = models.DecimalField(verbose_name='Sale price', blank=True,
                                     null=True, decimal_places=2, max_digits=10)
    drop_price = models.DecimalField(verbose_name='Dropshipper price', decimal_places=2, max_digits=10,
                                     blank=True, null=True)
    count = models.IntegerField(verbose_name='Count', default=0)
    is_new = models.BooleanField(verbose_name='New', default=False)
    is_sale = models.BooleanField(verbose_name='Sale', default=False)
    is_variability = models.BooleanField(verbose_name='Variability', default=False)

    sex = models.IntegerField(verbose_name='Sex', default=2, choices=SEX_CHOICES)
    status = models.IntegerField(verbose_name='Status', default=0, choices=STATUS_CHOICE)
    date_create = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    related_products = models.ManyToManyField('self', blank=True)
    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True, on_delete=models.SET_NULL)

    category = models.ManyToManyField(Category, blank=True)
    users = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name_product
