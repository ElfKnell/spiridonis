from rest_framework import serializers
from .models import Reviews


class ReviewsSerializers(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = '__all__'


class ReviewsDetailSerializers(serializers.ModelSerializer):

    class Meta:
        model = Reviews
        fields = ('title', 'message', 'date_add')
