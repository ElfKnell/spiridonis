from rest_framework import serializers

from product.serializers import ProductListCustomerSerializer
from .models import Set


class SetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Set
        fields = '__all__'


class SetListCustomerSerializer(serializers.ModelSerializer):
    main_product = ProductListCustomerSerializer(read_only=True)
    product_1 = ProductListCustomerSerializer(read_only=True)
    product_2 = ProductListCustomerSerializer(read_only=True)
    product_3 = ProductListCustomerSerializer(read_only=True)

    class Meta:
        model = Set
        exclude = ('opt_price', 'small_opt_price', 'drop_price')


class SetListWholesalerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Set
        exclude = ('price', 'sale_price', 'small_opt_price')


class SetListRetailWholesalerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Set
        exclude = ('price', 'sale_price', 'opt_price', 'drop_price')


class SetListDropshipperSerializer(serializers.ModelSerializer):

    class Meta:
        model = Set
        exclude = ('price', 'sale_price', 'small_opt_price', 'opt_price')
