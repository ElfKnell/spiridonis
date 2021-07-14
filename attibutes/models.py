from django.db import models
from product.models import Product
from vproduct.models import VProduct


class Attributes(models.Model):

    name_attributes = models.CharField(verbose_name='Name', max_length=30, unique=True)
    sort_order = models.IntegerField(verbose_name='Sort order', default=0)
    description = models.TextField(verbose_name='Description', blank=True, null=True)

    def __str__(self):
        return self.name_attributes


class AttributesValue(models.Model):
    name_value = models.CharField(verbose_name='Name Value', max_length=20)
    count = models.IntegerField(verbose_name='Count', default=1)
    description = models.TextField(verbose_name='Description', blank=True, null=True)

    name_attribute = models.ForeignKey(Attributes, blank=True, null=True, on_delete=models.CASCADE,
                                       verbose_name='Name attribute')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True,
                                related_name='attributes')
    v_product = models.ForeignKey(VProduct, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name_value
