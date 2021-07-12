from rest_framework import serializers

from rating.models import Rating, RatingStar


class RatingStarSerializer(serializers.ModelSerializer):

    class Meta:
        model = RatingStar
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ('star', 'product')

    def create(self, validated_data):
        rating = Rating.objects.update_or_create(
            ip=validated_data.get('ip', None),
            product=validated_data.get('product', None),
            defaults={'star': validated_data.get("star")}
        )
        return rating


class RatingListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = '__all__'
