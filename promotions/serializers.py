from .models import Promotions
from rest_framework import serializers


class EnBase:
    @staticmethod
    def get_product(obj):
        s = str(obj.product)
        st = s.split('-')
        if st[0] == "None":
            return ''
        return st[0]


class UkBase:
    @staticmethod
    def get_product(obj):
        s = str(obj.product)
        sl = s.split('-')
        if len(sl) < 2:
            return ''
        if sl[1] == "None":
            return ''
        return sl[1]


class RuBase:
    @staticmethod
    def get_product(obj):
        s = str(obj.product)
        sl = s.split('-')
        if len(sl) < 2 or len(sl) < 3:
            return ''
        if sl[2] == "None":
            return ''
        return sl[2]


class PromotionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promotions
        fields = '__all__'


class PromotionsListSerializer(serializers.ModelSerializer, EnBase):
    product = serializers.SerializerMethodField()

    class Meta:
        model = Promotions
        fields = ('name_promotions', 'sale', 'photo', 'product', 'slug')


class PromotionsUkListSerializer(serializers.ModelSerializer, UkBase):
    product = serializers.SerializerMethodField()

    class Meta:
        model = Promotions
        fields = ('name_promotions_uk', 'sale', 'photo', 'product', 'slug')


class PromotionsRuListSerializer(serializers.ModelSerializer, RuBase):
    product = serializers.SerializerMethodField()

    class Meta:
        model = Promotions
        fields = ('name_promotions_ru', 'sale', 'photo', 'product', 'slug')


class PromotionsDetailSerializer(serializers.ModelSerializer, EnBase):
    product = serializers.SerializerMethodField()

    class Meta:
        model = Promotions
        fields = ('name_promotions', 'sale', 'photo', 'product', 'title')


class PromotionsUkDetailSerializer(serializers.ModelSerializer, UkBase):
    product = serializers.SerializerMethodField()

    class Meta:
        model = Promotions
        fields = ('name_promotions_uk', 'sale', 'photo', 'product', 'title')


class PromotionsRuDetailSerializer(serializers.ModelSerializer, RuBase):
    product = serializers.SerializerMethodField()

    class Meta:
        model = Promotions
        fields = ('name_promotions_ru', 'sale', 'photo', 'product', 'title')
