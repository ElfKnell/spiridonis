from django.db import models
from django.contrib.auth import get_user_model
from product.models import Product

User = get_user_model()


class Reviews(models.Model):
    title = models.CharField(verbose_name='Title', max_length=50)
    message = models.TextField(verbose_name='Message')
    date_add = models.DateTimeField(verbose_name='Date', auto_now_add=True)
    status = models.BooleanField(verbose_name='Status', default=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.message
