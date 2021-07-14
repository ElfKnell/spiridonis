from rest_framework import serializers

from product.serializers import ProductListSerializer
from .models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name_category', 'photo', 'description', 'title', 'parent_category',
                  'filters.py', 'status', 'updated_on')


class CategoryListSerializer(serializers.ModelSerializer):
    product = ProductListSerializer(many=True)

    class Meta:
        model = Category
        fields = ('id', 'name_category', 'parent_category', 'product')
