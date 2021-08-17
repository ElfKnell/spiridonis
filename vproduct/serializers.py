from rest_framework import serializers
from .models import VProduct


class VProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = VProduct
        fields = '__all__'


class VProductCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = VProduct
        fields = ['article', 'price', 'sale_price', 'weight']


class VProductWholesalerSerializer(serializers.ModelSerializer):

    class Meta:
        model = VProduct
        fields = ['article', 'opt_price', 'weight']


class VProductRetailWholesalerSerializer(serializers.ModelSerializer):

    class Meta:
        model = VProduct
        fields = ['article', 'small_opt_price', 'weight']


class VProductDropshipperSerializer(serializers.ModelSerializer):

    class Meta:
        model = VProduct
        fields = ['article', 'drop_price', 'weight']
