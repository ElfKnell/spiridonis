from rest_framework import serializers
from .models import VProduct


class VPorductSerializer(serializers.ModelSerializer):

    class Meta:
        model = VProduct
        fields = '__all__'
