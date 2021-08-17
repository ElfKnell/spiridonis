from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class CompanyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        exclude = ('users', 'uk_name_company', 'ru_name_company', 'uk_description', 'ru_description', 'uk_address',
                   'ru_address', 'uk_operating_mode', 'ru_operating_mode')


class CompanyListUkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        exclude = ('users', 'name_company', 'ru_name_company', 'description', 'ru_description', 'address',
                   'ru_address', 'operating_mode', 'ru_operating_mode')


class CompanyListRuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        exclude = ('users', 'uk_name_company', 'name_company', 'uk_description', 'description', 'uk_address',
                   'address', 'uk_operating_mode', 'operating_mode')
