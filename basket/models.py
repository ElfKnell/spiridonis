from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product
from vproduct.models import VProduct

User = get_user_model()


STATUS_CHOICES = (
    (1, 'in processing'),
    (2, 'accepted'),
    (3, 'on maintenance'),
    (4, 'sent'),
    (5, 'done'),
    (6, 'canceled'),
    (7, 'deleted')
)
STATUS_CHOICES_UK = (
    (1, 'в процесі'),
    (2, 'прийнято'),
    (3, 'в обробці'),
    (4, 'відправлено'),
    (5, 'зроблено'),
    (6, 'скасовано'),
    (7, 'видалено')
)
STATUS_CHOICES_RU = (
    (1, 'в процессе'),
    (2, 'принято'),
    (3, 'в обработке'),
    (4, 'отправлено'),
    (5, 'сделано'),
    (6, 'отменен'),
    (7, 'удалено')
)
PAYMENT_CHOICE = (
    (1, 'to a bank card'),
    (2, 'C. O. D.')
)
PAYMENT_CHOICE_UK = (
    (1, 'на банківську картку'),
    (2, 'акладний платіж')
)
PAYMENT_CHOICE_RU = (
    (1, 'на банковскую карту'),
    (2, 'наложный платеж')
)


class Basket(models.Model):
    count = models.IntegerField(verbose_name='Count', default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vproduct = models.ForeignKey(VProduct, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.product.name_product}"


class Order(models.Model):
    basket = models.ManyToManyField(Basket)
    number_order = models.CharField(max_length=10)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    status_uk = models.IntegerField(choices=STATUS_CHOICES_UK, default=1)
    status_ru = models.IntegerField(choices=STATUS_CHOICES_RU, default=1)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    type_payment = models.IntegerField(choices=PAYMENT_CHOICE, default=2)
    type_payment_uk = models.IntegerField(choices=PAYMENT_CHOICE_UK, default=2)
    type_payment_ru = models.IntegerField(choices=PAYMENT_CHOICE_RU, default=2)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=3)
    sale = models.IntegerField(default=0)


class Selection(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    vproduct = models.ForeignKey(VProduct, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date_create = models.DateTimeField(auto_now_add=True)
