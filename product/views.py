from django.db.models import Avg
from django.db.models.functions import Round
from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter

from .serializers import ProductSerializers, ProductDetailSerializers, ProductListSerializer
from users.permissions import IsEditorUser
from .models import Product
from rating.service import get_client_ip


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializers
    #permission_classes = [IsEditorUser]


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    filter_backends = [SearchFilter, ]
    search_fields = ['name_product', 'model', 'article', ]
    pagination_by = 25
    queryset = Product.objects.annotate(middle_star=Round(Avg('rating__star')))


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializers
    queryset = Product.objects.all()
    permission_classes = [IsEditorUser]

