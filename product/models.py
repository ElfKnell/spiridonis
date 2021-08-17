from django import forms
from django.db import models
from django.contrib.auth import get_user_model

from category.models import Category
from manufacturer.models import Manufacturer


User = get_user_model()


SEX_CHOICES = [
    (0, 'children'),
    (1, 'man'),
    (2, 'woman'),
    (3, 'unisex')
]
SEX_CHOICES_UK = [
    (0, 'дитячі'),
    (1, 'чоловічі'),
    (2, 'жіночі'),
    (3, 'унісекс')
]
SEX_CHOICES_RU = [
    (0, 'детские'),
    (1, 'мужские'),
    (2, 'женские'),
    (3, 'унисекс')
]
STATUS_CHOICE = [
    (0, 'is available'),
    (1, 'not available'),
    (2, 'in order')
]
STATUS_CHOICE_UK = [
    (0, 'в наявності'),
    (1, 'немає в наявності'),
    (2, 'під замовлення')
]
STATUS_CHOICE_RU = [
    (0, 'в наличии'),
    (1, 'нет в наличии'),
    (2, 'под заказ')
]


class Product(models.Model):

    name_product = models.CharField(verbose_name='Name', unique=True, max_length=30)
    name_product_uk = models.CharField(verbose_name='Назва', unique=True, max_length=30,
                                       null=True, blank=True)
    name_product_ru = models.CharField(verbose_name='Название', unique=True, max_length=30,
                                       null=True, blank=True)
    title = models.CharField(verbose_name='Title', max_length=30, unique=True)
    article = models.CharField(verbose_name='Article', max_length=30, unique=True)
    slug = models.SlugField(verbose_name='Part of the link', max_length=30, unique=True)
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    description_uk = models.TextField(verbose_name='Опис', blank=True, null=True)
    description_ru = models.TextField(verbose_name='Описание', blank=True, null=True)
    meta_description = models.CharField(verbose_name='Meta-description', max_length=120,
                                        blank=True, null=True)
    photo = models.ImageField(verbose_name='Photo', blank=True, null=True, upload_to='product_photo')
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
    sex_uk = models.IntegerField(verbose_name='Стать', default=2, choices=SEX_CHOICES_UK)
    sex_ru = models.IntegerField(verbose_name='Пол', default=2, choices=SEX_CHOICES_RU)
    status = models.IntegerField(verbose_name='Status', default=0, choices=STATUS_CHOICE)
    status_uk = models.IntegerField(verbose_name='Статус', default=0, choices=STATUS_CHOICE_UK)
    status_ru = models.IntegerField(verbose_name='Статус', default=0, choices=STATUS_CHOICE_RU)
    date_create = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    related_products = models.ManyToManyField('self', blank=True)
    manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True, on_delete=models.SET_NULL)

    category = models.ManyToManyField(Category, blank=True, related_name='product')
    users = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.name_product}-{self.name_product_uk}-{self.name_product_ru}"
