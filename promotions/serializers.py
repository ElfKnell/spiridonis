from .models import Promotions
from rest_framework import serializers


class PromotionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promotions
        fields = '__all__'
