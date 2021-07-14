from django.shortcuts import render
from rest_framework import generics
from .serializers import VProductSerializer
from .models import VProduct
from users.permissions import IsEditorUser


class VProductCreateView(generics.CreateAPIView):
    serializer_class = VProductSerializer
    #permission_classes = [IsEditorUser, ]


class VProductListView(generics.ListAPIView):
    serializer_class = VProductSerializer
    queryset = VProduct.objects.all()
    #permission_classes = [IsEditorUser, ]


class VProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = VProductSerializer
    queryset = VProduct.objects.all()
    #permission_classes = [IsEditorUser, ]