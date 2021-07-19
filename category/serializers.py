from rest_framework import serializers

from product.serializers import ProductListCustomerSerializer, ProductListWholesalerSerializer, \
    ProductListRetailWholesalerSerializer, ProductListDropshipperSerializer
from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name_category', 'photo', 'description', 'title', 'parent_category',
                  'status')


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name_category', 'parent_category')


class CategoryCustomerDetailSerializer(serializers.ModelSerializer):
    product = ProductListCustomerSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name_category', 'photo', 'description', 'title', 'parent_category',
                  'status', 'product')


class CategoryWholesalerDetailSerializer(serializers.ModelSerializer):
    product = ProductListWholesalerSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name_category', 'photo', 'description', 'title', 'parent_category',
                  'status', 'product')


class CategoryRetailWholesalerDetailSerializer(serializers.ModelSerializer):
    product = ProductListRetailWholesalerSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name_category', 'photo', 'description', 'title', 'parent_category',
                  'status', 'product')


class CategoryDropshipperDetailSerializer(serializers.ModelSerializer):
    product = ProductListDropshipperSerializer(many=True)
    middle_star = serializers.IntegerField(default=0)

    class Meta:
        model = Category
        fields = ('id', 'name_category', 'photo', 'description', 'title', 'parent_category',
                  'status', 'product', 'middle_star')
