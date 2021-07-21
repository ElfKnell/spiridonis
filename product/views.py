from django.contrib.auth.models import AnonymousUser
from django.db.models import Avg
from django.db.models.functions import Round
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
from .filter import PriceFilter

from .serializers import ProductSerializers, ProductDetailSerializers, ProductListSerializer, \
    ProductListCustomerSerializer, ProductListWholesalerSerializer, ProductListRetailWholesalerSerializer, \
    ProductListDropshipperSerializer, ProductDetailCustomerSerializers
from users.permissions import IsEditorUser
from .models import Product


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializers
    permission_classes = [IsEditorUser]


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name_product', 'model', 'article', ]
    filterset_class = PriceFilter
    pagination_by = 25
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser):
            return ProductListCustomerSerializer
        else:
            if self.request.user.role == 2:
                return ProductListSerializer
            if self.request.user.role == 3:
                return ProductListCustomerSerializer
            if self.request.user.role == 4:
                return ProductListWholesalerSerializer
            if self.request.user.role == 5:
                return ProductListRetailWholesalerSerializer
            if self.request.user.role == 6:
                return ProductListDropshipperSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.annotate(middle_star=Round(Avg('rating__star')))

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser):
            return ProductDetailCustomerSerializers
        else:
            if self.request.user.role == 2:
                return ProductDetailSerializers
            if self.request.user.role == 3:
                return ProductDetailCustomerSerializers
            if self.request.user.role == 4:
                return ProductListWholesalerSerializer
            if self.request.user.role == 5:
                return ProductListRetailWholesalerSerializer
            if self.request.user.role == 6:
                return ProductListDropshipperSerializer

    permission_classes = [IsEditorUser, ]
