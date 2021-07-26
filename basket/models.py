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
    date_create = models.DateTimeField(auto_now_add=True)

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.product.name_product} and {self.user.last_name}"


class Order(models.Model):
    basket = models.ManyToManyField(Basket)
    number_order = models.CharField(max_length=10)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    type_payment = models.IntegerField(choices=PAYMENT_CHOICE, default=2)


class Selection(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date_create = models.DateTimeField(auto_now_add=True)
