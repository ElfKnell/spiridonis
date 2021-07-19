from django.db.models import Avg
from django.db.models.functions import Round
from rest_framework import serializers
from .models import Product
from attibutes.serializers import AttributeValueCustomerListSerializer, \
    AttributeValueWholesalerListSerializer, AttributeValueRetailWholesalerListSerializer, \
    AttributeValueDropshipperListSerializer, AttributeValueListSerializer, AttributeValueAllListSerializer
from rating.serializers import RatingListSerializer, RatingStarSerializer


class ProductSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


# Відображення каталога товарів
class ProductListSerializer(serializers.ModelSerializer):
    attributes = AttributeValueAllListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)
    rating = RatingListSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class ProductListCustomerSerializer(serializers.ModelSerializer):
    attributes = AttributeValueListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)
    rating = RatingStarSerializer(many=True)
    #middle_star = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name_product', 'article', 'photo', 'price',
                  'sale_price', 'attributes', 'rating', 'middle_star')


class ProductListWholesalerSerializer(serializers.ModelSerializer):
    attributes = AttributeValueListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = ('id', 'name_product', 'article', 'photo', 'opt_price',
                  'attributes', 'middle_star')


class ProductListRetailWholesalerSerializer(serializers.ModelSerializer):
    attributes = AttributeValueListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = ('id', 'name_product', 'article', 'photo', 'small_opt_price',
                  'attributes', 'middle_star')


class ProductListDropshipperSerializer(serializers.ModelSerializer):
    attributes = AttributeValueListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        fields = ('id', 'name_product', 'article', 'photo',
                  'drop_price', 'attributes', 'middle_star')
#Кінець відображення каталогу товарів


#Відображення окремого товару
class ProductDetailSerializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        exclude = ('date_create', 'updated_on')


class ProductDetailCustomerSerializers(serializers.ModelSerializer):
    attributes = AttributeValueCustomerListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        exclude = ('date_create', 'updated_on', 'users', 'opt_price', 'small_opt_price',
                   'drop_price', 'is_new', 'is_variability', 'status', 'count')


class ProductDetailWholesalerSerializer(serializers.ModelSerializer):
    attributes = AttributeValueWholesalerListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        exclude = ('date_create', 'updated_on', 'users', 'price', 'small_opt_price',
                   'drop_price', 'sale_price', 'is_new', 'is_sale', 'is_variability', 'status', 'count')


class ProductDetailRetailWholesalerSerializer(serializers.ModelSerializer):
    attributes = AttributeValueRetailWholesalerListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        exclude = ('date_create', 'updated_on', 'users', 'opt_price', 'price',
                   'drop_price', 'sale_price', 'is_new', 'is_sale', 'is_variability', 'status', 'count')


class ProductDetailDropshipperSerializer(serializers.ModelSerializer):
    attributes = AttributeValueDropshipperListSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Product
        exclude = ('date_create', 'updated_on', 'users', 'opt_price', 'small_opt_price',
                   'price', 'sale_price', 'is_new', 'is_sale', 'is_variability', 'status', 'count')
#Кінець відображення окремого товару
