from rest_framework import serializers

from product.serializers import ProductListCustomerSerializer, ProductListWholesalerSerializer, \
    ProductListRetailWholesalerSerializer, ProductListDropshipperSerializer, ProductListSerializer
from .models import Set


class SetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Set
        fields = '__all__'


#Відображення каталогу наборів
class SetListCustomerSerializer(serializers.ModelSerializer):
    main_product = ProductListCustomerSerializer(read_only=True)
    product_1 = ProductListCustomerSerializer(read_only=True)
    product_2 = ProductListCustomerSerializer(read_only=True)
    product_3 = ProductListCustomerSerializer(read_only=True)

    class Meta:
        model = Set
        exclude = ('opt_price', 'small_opt_price', 'drop_price', 'date_create', 'updated_on')


class SetListWholesalerSerializer(serializers.ModelSerializer):
    main_product = ProductListWholesalerSerializer(read_only=True)
    product_1 = ProductListWholesalerSerializer(read_only=True)
    product_2 = ProductListWholesalerSerializer(read_only=True)
    product_3 = ProductListWholesalerSerializer(read_only=True)

    class Meta:
        model = Set
        exclude = ('price', 'sale_price', 'small_opt_price', 'date_create', 'updated_on')


class SetListRetailWholesalerSerializer(serializers.ModelSerializer):
    main_product = ProductListRetailWholesalerSerializer(read_only=True)
    product_1 = ProductListRetailWholesalerSerializer(read_only=True)
    product_2 = ProductListRetailWholesalerSerializer(read_only=True)
    product_3 = ProductListRetailWholesalerSerializer(read_only=True)

    class Meta:
        model = Set
        exclude = ('price', 'sale_price', 'opt_price', 'drop_price', 'date_create', 'updated_on')


class SetListDropshipperSerializer(serializers.ModelSerializer):
    main_product = ProductListDropshipperSerializer(read_only=True)
    product_1 = ProductListDropshipperSerializer(read_only=True)
    product_2 = ProductListDropshipperSerializer(read_only=True)
    product_3 = ProductListDropshipperSerializer(read_only=True)

    class Meta:
        model = Set
        exclude = ('price', 'sale_price', 'small_opt_price', 'opt_price', 'date_create', 'updated_on')


class SetListSerializer(serializers.ModelSerializer):
    main_product = ProductListSerializer(read_only=True)
    product_1 = ProductListSerializer(read_only=True)
    product_2 = ProductListSerializer(read_only=True)
    product_3 = ProductListSerializer(read_only=True)

    class Meta:
        model = Set
        fields = '__all__'
#Кінець відображення каталогу наборів


#Відображення наборів