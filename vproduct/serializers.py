from rest_framework import serializers
from .models import VProduct


class VProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = VProduct
        fields = '__all__'


class VProductCustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = VProduct
        fields = ['article', 'description', 'price', 'sale_price', 'weight']


class VProductWholesalerSerializer(serializers.ModelSerializer):

    class Meta:
        model = VProduct
        fields = ['article', 'description', 'opt_price', 'weight']


class VProductRetailWholesalerSerializer(serializers.ModelSerializer):

    class Meta:
        model = VProduct
        fields = ['article', 'description', 'small_opt_price', 'weight']


class VProductDropshipperSerializer(serializers.ModelSerializer):

    class Meta:
        model = VProduct
        fields = ['article', 'description', 'drop_price', 'weight']
