from rest_framework import serializers

from product.serializers import ProductListCustomerSerializer, ProductListWholesalerSerializer, \
    ProductListRetailWholesalerSerializer, ProductListDropshipperSerializer, ProductListSerializer, \
    ProductUkListCustomerSerializer, ProductRuListCustomerSerializer, ProductUkListWholesalerSerializer, \
    ProductRuListWholesalerSerializer, ProductUkListRetailWholesalerSerializer, ProductRuListRetailWholesalerSerializer, \
    ProductUkListDropshipperSerializer, ProductRuListDropshipperSerializer
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
        exclude = ('opt_price', 'small_opt_price', 'drop_price', 'date_create', 'updated_on',
                   'name_set_uk', 'name_set_ru', 'description_uk', 'description_ru')


class SetListUkCustomerSerializer(serializers.ModelSerializer):
    main_product = ProductUkListCustomerSerializer(read_only=True)
    product_1 = ProductUkListCustomerSerializer(read_only=True)
    product_2 = ProductUkListCustomerSerializer(read_only=True)
    product_3 = ProductUkListCustomerSerializer(read_only=True)

    class Meta:
        model = Set
        exclude = ('opt_price', 'small_opt_price', 'drop_price', 'date_create', 'updated_on',
                   'name_set', 'name_set_ru', 'description', 'description_ru')


class SetListRuCustomerSerializer(serializers.ModelSerializer):
    main_product = ProductRuListCustomerSerializer(read_only=True)
    product_1 = ProductRuListCustomerSerializer(read_only=True)
    product_2 = ProductRuListCustomerSerializer(read_only=True)
    product_3 = ProductRuListCustomerSerializer(read_only=True)

    class Meta:
        model = Set
        exclude = ('opt_price', 'small_opt_price', 'drop_price', 'date_create', 'updated_on',
                   'name_set_uk', 'name_set', 'description_uk', 'description')


class SetListWholesalerSerializer(serializers.ModelSerializer):
    main_product = ProductListWholesalerSerializer(read_only=True)
    product_1 = ProductListWholesalerSerializer(read_only=True)
    product_2 = ProductListWholesalerSerializer(read_only=True)
    product_3 = ProductListWholesalerSerializer(read_only=True)

    class Meta:
        model = Set
        exclude = ('price', 'sale_price', 'small_opt_price', 'date_create', 'updated_on',
                   'name_set_uk', 'name_set_ru', 'description_uk', 'description_ru', 'drop_price')


class SetListUkWholesalerSerializer(serializers.ModelSerializer):
    main_product = ProductUkListWholesalerSerializer(read_only=True)
    product_1 = ProductUkListWholesalerSerializer(read_only=True)
    product_2 = ProductUkListWholesalerSerializer(read_only=True)
    product_3 = ProductUkListWholesalerSerializer(read_only=True)

    class Meta:
        model = Set
        exclude = ('price', 'sale_price', 'small_opt_price', 'date_create', 'updated_on',
                   'name_set', 'name_set_ru', 'description', 'description_ru', 'drop_price')


class SetListRuWholesalerSerializer(serializers.ModelSerializer):
    main_product = ProductRuListWholesalerSerializer(read_only=True)
    product_1 = ProductRuListWholesalerSerializer(read_only=True)
    product_2 = ProductRuListWholesalerSerializer(read_only=True)
    product_3 = ProductRuListWholesalerSerializer(read_only=True)

    class Meta:
        model = Set
        exclude = ('price', 'sale_price', 'small_opt_price', 'date_create', 'updated_on',
                   'name_set_uk', 'name_set', 'description_uk', 'description', 'drop_price')


class SetListRetailWholesalerSerializer(serializers.ModelSerializer):
    main_product = ProductListRetailWholesalerSerializer(read_only=True)
    product_1 = ProductListRetailWholesalerSerializer(read_only=True)
    product_2 = ProductListRetailWholesalerSerializer(read_only=True)
    product_3 = ProductListRetailWholesalerSerializer(read_only=True)

    class Meta:
        model = Set
        exclude = ('price', 'sale_price', 'opt_price', 'drop_price', 'date_create', 'updated_on',
                   'name_set_uk', 'name_set_ru', 'description_uk', 'description_ru')


class SetListUkRetailWholesalerSerializer(serializers.ModelSerializer):
    main_product = ProductUkListRetailWholesalerSerializer(read_only=True)
    product_1 = ProductUkListRetailWholesalerSerializer(read_only=True)
    product_2 = ProductUkListRetailWholesalerSerializer(read_only=True)
    product_3 = ProductUkListRetailWholesalerSerializer(read_only=True)

    class Meta:
        model = Set
        exclude = ('price', 'sale_price', 'opt_price', 'drop_price', 'date_create', 'updated_on',
                   'name_set', 'name_set_ru', 'description', 'description_ru')


class SetListRuRetailWholesalerSerializer(serializers.ModelSerializer):
    main_product = ProductRuListRetailWholesalerSerializer(read_only=True)
    product_1 = ProductRuListRetailWholesalerSerializer(read_only=True)
    product_2 = ProductRuListRetailWholesalerSerializer(read_only=True)
    product_3 = ProductRuListRetailWholesalerSerializer(read_only=True)

    class Meta:
        model = Set
        exclude = ('price', 'sale_price', 'opt_price', 'drop_price', 'date_create', 'updated_on',
                   'name_set_uk', 'name_set', 'description_uk', 'description')


class SetListDropshipperSerializer(serializers.ModelSerializer):
    main_product = ProductListDropshipperSerializer(read_only=True)
    product_1 = ProductListDropshipperSerializer(read_only=True)
    product_2 = ProductListDropshipperSerializer(read_only=True)
    product_3 = ProductListDropshipperSerializer(read_only=True)

    class Meta:
        model = Set
        exclude = ('price', 'sale_price', 'small_opt_price', 'opt_price', 'date_create', 'updated_on',
                   'name_set_uk', 'name_set_ru', 'description_uk', 'description_ru')


class SetListUkDropshipperSerializer(serializers.ModelSerializer):
    main_product = ProductUkListDropshipperSerializer(read_only=True)
    product_1 = ProductUkListDropshipperSerializer(read_only=True)
    product_2 = ProductUkListDropshipperSerializer(read_only=True)
    product_3 = ProductUkListDropshipperSerializer(read_only=True)

    class Meta:
        model = Set
        exclude = ('price', 'sale_price', 'small_opt_price', 'opt_price', 'date_create', 'updated_on',
                   'name_set', 'name_set_ru', 'description', 'description_ru')


class SetListRuDropshipperSerializer(serializers.ModelSerializer):
    main_product = ProductRuListDropshipperSerializer(read_only=True)
    product_1 = ProductRuListDropshipperSerializer(read_only=True)
    product_2 = ProductRuListDropshipperSerializer(read_only=True)
    product_3 = ProductRuListDropshipperSerializer(read_only=True)

    class Meta:
        model = Set
        exclude = ('price', 'sale_price', 'small_opt_price', 'opt_price', 'date_create', 'updated_on',
                   'name_set_uk', 'name_set', 'description_uk', 'description')


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