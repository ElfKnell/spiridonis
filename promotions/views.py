from django.shortcuts import render
from .models import Promotions
from .serializers import PromotionsSerializer
from rest_framework import generics


class PromotionsCreateView(generics.CreateAPIView):
    serializer_class = PromotionsSerializer
    permission_classes = []


class PromotionsListView(generics.ListAPIView):
    serializer_class = PromotionsSerializer
    queryset = Promotions.objects.all()
    permission_classes = []


class PromotionsDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PromotionsSerializer
    queryset = Promotions.objects.all()
    permission_classes = []
