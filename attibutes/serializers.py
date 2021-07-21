from rest_framework import serializers
from .models import AttributesValue, Attributes
from vproduct.serializers import VProductWholesalerSerializer, VProductCustomerSerializer, \
    VProductRetailWholesalerSerializer, VProductDropshipperSerializer, VProductSerializer


class AttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attributes
        fields = '__all__'


class AttributeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attributes
        fields = ('name_attributes',)


class AttributeValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttributesValue
        fields = '__all__'


class AttributeValueWholesalerListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeListSerializer(read_only=True)
    v_product = VProductWholesalerSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value', 'v_product', 'product')


class AttributeValueCustomerListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeListSerializer(read_only=True)
    v_product = VProductCustomerSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value', 'v_product', 'product')


class AttributeValueDropshipperListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeListSerializer(read_only=True)
    v_product = VProductDropshipperSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value', 'v_product', 'product')


class AttributeValueRetailWholesalerListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeListSerializer(read_only=True)
    v_product = VProductRetailWholesalerSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value', 'v_product', 'product')


class AttributeValueListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeListSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value')


class AttributeValueAllListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeListSerializer(read_only=True)
    v_product = VProductSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = '__all__'
