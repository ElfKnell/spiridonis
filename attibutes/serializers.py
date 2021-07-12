from rest_framework import serializers
from .models import AttributesValue, Attributes, AttributeVariant
from vproduct.serializers import VPorductSerializer


class AttributeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attributes
        fields = '__all__'


class AttributeListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Attributes
        fields = ('name_attributes', )


class AttributeValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttributesValue
        fields = '__all__'


class AttributeValueListSerializer(serializers.ModelSerializer):
    name_attribute = AttributeListSerializer(read_only=True)

    class Meta:
        model = AttributesValue
        fields = ('name_attribute', 'name_value')


class AttributeVariantSerializer(serializers.ModelSerializer):

    attribute_values = AttributeValueSerializer(read_only=False)
    v_product = VPorductSerializer(read_only=False)

    class Meta:
        model = AttributeVariant
        fields = '__all__'
