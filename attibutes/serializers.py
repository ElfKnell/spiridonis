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


class AttributeUkListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attributes
        fields = ('name_attributes_uk',)


class AttributeRuListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attributes
        fields = ('name_attributes_ru',)


class AttributeValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttributesValue
        fields = '__all__'


class AttributeValueCustomerListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeListSerializer(read_only=True)
    v_product = VProductCustomerSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value', 'v_product', 'product')


class AttributeValueCustomerUkListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeUkListSerializer(read_only=True)
    v_product = VProductCustomerSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value_uk', 'v_product', 'product')


class AttributeValueCustomerRuListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeRuListSerializer(read_only=True)
    v_product = VProductCustomerSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value_ru', 'v_product', 'product')


class AttributeValueWholesalerListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeListSerializer(read_only=True)
    v_product = VProductWholesalerSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value', 'v_product', 'product')


class AttributeValueWholesalerUkListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeUkListSerializer(read_only=True)
    v_product = VProductWholesalerSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value_uk', 'v_product', 'product')


class AttributeValueWholesalerRuListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeRuListSerializer(read_only=True)
    v_product = VProductWholesalerSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value_ru', 'v_product', 'product')


class AttributeValueRetailWholesalerListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeListSerializer(read_only=True)
    v_product = VProductRetailWholesalerSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value', 'v_product', 'product')


class AttributeValueRetailWholesalerUkListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeUkListSerializer(read_only=True)
    v_product = VProductRetailWholesalerSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value_uk', 'v_product', 'product')


class AttributeValueRetailWholesalerRuListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeRuListSerializer(read_only=True)
    v_product = VProductRetailWholesalerSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value_ru', 'v_product', 'product')


class AttributeValueDropshipperListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeListSerializer(read_only=True)
    v_product = VProductDropshipperSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value', 'v_product', 'product')


class AttributeValueDropshipperUkListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeUkListSerializer(read_only=True)
    v_product = VProductDropshipperSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value_uk', 'v_product', 'product')


class AttributeValueDropshipperRuListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeRuListSerializer(read_only=True)
    v_product = VProductDropshipperSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value_ru', 'v_product', 'product')


class AttributeValueListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeListSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value')


class AttributeValueUkListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeUkListSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value_uk')


class AttributeValueRuListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeRuListSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value_ru')


class AttributeValueAllListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeListSerializer(read_only=True)
    v_product = VProductSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = '__all__'
