from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = '__all__'


class NewsEnDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        exclude = ('users', 'uk_post', 'ru_post', 'uk_text', 'ru_text')


class NewsUkDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        exclude = ('users', 'post', 'ru_post', 'text', 'ru_text')


class NewsRuDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        exclude = ('users', 'uk_post', 'post', 'uk_text', 'text')


class NewsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        exclude = ('users', )


class NewsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'post', 'photo', 'part_link')


class NewsUkListSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'uk_post', 'photo', 'part_link')


class NewsRuListSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ('id', 'ru_post', 'photo', 'part_link')
