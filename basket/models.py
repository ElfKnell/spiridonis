from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product

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
PAYMENT_CHOICE = (
    (1, 'to a bank card'),
    (2, 'C. O. D.')
)


class Basket(models.Model):
    count = models.IntegerField(verbose_name='Count', default=1)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.name_product}"


class Order(models.Model):
    basket = models.ManyToManyField(Basket)
    number_order = models.CharField(max_length=10)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    type_payment = models.IntegerField(choices=PAYMENT_CHOICE, default=2)
    user = models.ForeignKey(User, on_delete=models.PROTECT, default=3)
    sale = models.IntegerField(default=0)


class Selection(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date_create = models.DateTimeField(auto_now_add=True)
