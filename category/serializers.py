from rest_framework import serializers

from product.serializers import ProductListCustomerSerializer, ProductListWholesalerSerializer, \
    ProductListRetailWholesalerSerializer, ProductListDropshipperSerializer, ProductUkListCustomerSerializer, \
    ProductRuListCustomerSerializer, ProductUkListWholesalerSerializer, ProductRuListWholesalerSerializer, \
    ProductUkListRetailWholesalerSerializer, ProductRuListRetailWholesalerSerializer, \
    ProductUkListDropshipperSerializer, ProductRuListDropshipperSerializer
from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('date_create', 'updated_on', 'users')


class EnBase:
    @staticmethod
    def get_parent_category(obj):
        s = str(obj.parent_category)
        st = s.split('-')
        if st[0] == "None":
            return ''
        return st[0]


class UkBase:
    @staticmethod
    def get_parent_category(obj):
        s = str(obj.parent_category)
        sl = s.split('-')
        if len(sl) < 2:
            return ''
        if sl[1] == "None":
            return ''
        return sl[1]


class RuBase:
    @staticmethod
    def get_parent_category(obj):
        s = str(obj.parent_category)
        sl = s.split('-')
        if len(sl) < 2 or len(sl) < 3:
            return ''
        if sl[2] == "None":
            return ''
        return sl[2]


class CategoryListSerializer(serializers.ModelSerializer, EnBase):
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name_category', 'parent_category', 'slug')


class CategoryListUkSerializer(serializers.ModelSerializer, UkBase):
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'uk_name_category', 'parent_category', 'slug')


class CategoryListRUSerializer(serializers.ModelSerializer, RuBase):
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'ru_name_category', 'parent_category', 'slug')


class CategoryCustomerDetailSerializer(serializers.ModelSerializer, EnBase):
    product = ProductListCustomerSerializer(many=True)
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name_category', 'photo', 'description', 'title', 'parent_category',
                  'status', 'product')


class CategoryCustomerUkDetailSerializer(serializers.ModelSerializer, UkBase):
    product = ProductUkListCustomerSerializer(many=True)
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'uk_name_category', 'photo', 'uk_description', 'title', 'parent_category',
                  'status', 'product')


class CategoryCustomerRuDetailSerializer(serializers.ModelSerializer, RuBase):
    product = ProductRuListCustomerSerializer(many=True)
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'ru_name_category', 'photo', 'ru_description', 'title', 'parent_category',
                  'status', 'product')


class CategoryWholesalerDetailSerializer(serializers.ModelSerializer, EnBase):
    product = ProductListWholesalerSerializer(many=True)
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name_category', 'photo', 'description', 'title', 'parent_category',
                  'status', 'product')


class CategoryWholesalerUkDetailSerializer(serializers.ModelSerializer, UkBase):
    product = ProductUkListWholesalerSerializer(many=True)
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'uk_name_category', 'photo', 'uk_description', 'title', 'parent_category',
                  'status', 'product')


class CategoryWholesalerRuDetailSerializer(serializers.ModelSerializer, RuBase):
    product = ProductRuListWholesalerSerializer(many=True)
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'ru_name_category', 'photo', 'ru_description', 'title', 'parent_category',
                  'status', 'product')


class CategoryRetailWholesalerDetailSerializer(serializers.ModelSerializer, EnBase):
    product = ProductListRetailWholesalerSerializer(many=True)
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name_category', 'photo', 'description', 'title', 'parent_category',
                  'status', 'product')


class CategoryRetailWholesalerUkDetailSerializer(serializers.ModelSerializer, UkBase):
    product = ProductUkListRetailWholesalerSerializer(many=True)
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'uk_name_category', 'photo', 'uk_description', 'title', 'parent_category',
                  'status', 'product')


class CategoryRetailWholesalerRuDetailSerializer(serializers.ModelSerializer, RuBase):
    product = ProductRuListRetailWholesalerSerializer(many=True)
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'ru_name_category', 'photo', 'ru_description', 'title', 'parent_category',
                  'status', 'product')


class CategoryDropshipperDetailSerializer(serializers.ModelSerializer, EnBase):
    product = ProductListDropshipperSerializer(many=True)
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name_category', 'photo', 'description', 'title', 'parent_category',
                  'status', 'product')


class CategoryDropshipperUkDetailSerializer(serializers.ModelSerializer, UkBase):
    product = ProductUkListDropshipperSerializer(many=True)
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'uk_name_category', 'photo', 'uk_description', 'title', 'parent_category',
                  'status', 'product')


class CategoryDropshipperRuDetailSerializer(serializers.ModelSerializer, RuBase):
    product = ProductRuListDropshipperSerializer(many=True)
    parent_category = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'ru_name_category', 'photo', 'ru_description', 'title', 'parent_category',
                  'status', 'product')
