from django.shortcuts import render
from rest_framework import generics
from .serializers import VPorductSerializer
from .models import VProduct
from users.permissions import IsEditorUser


class VProductCreateView(generics.CreateAPIView):
    serializer_class = VPorductSerializer
    #permission_classes = [IsEditorUser, ]


class VProductListView(generics.ListAPIView):
    serializer_class = VPorductSerializer
    queryset = VProduct.objects.all()
    #permission_classes = [IsEditorUser, ]


class VProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VPorductSerializer
    queryset = VProduct.objects.all()
    #permission_classes = [IsEditorUser, ]