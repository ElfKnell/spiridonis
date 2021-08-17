from django.contrib.auth.models import AnonymousUser
from django.db.models import Avg
from django.db.models.functions import Round
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
from .filter import PriceFilter

from .serializers import ProductSerializers, ProductDetailSerializers, ProductListSerializer, \
    ProductListCustomerSerializer, ProductListWholesalerSerializer, ProductListRetailWholesalerSerializer, \
    ProductListDropshipperSerializer, ProductDetailCustomerSerializers, ProductUkListCustomerSerializer, \
    ProductRuListCustomerSerializer, ProductUkListWholesalerSerializer, ProductRuListWholesalerSerializer, \
    ProductRuListDropshipperSerializer, ProductUkListDropshipperSerializer, ProductRuListRetailWholesalerSerializer, \
    ProductUkListRetailWholesalerSerializer, ProductUkDetailCustomerSerializers, ProductRuDetailCustomerSerializers, \
    ProductUkDetailDropshipperSerializer, ProductRuDetailDropshipperSerializer, \
    ProductRuDetailRetailWholesalerSerializer, ProductUkDetailRetailWholesalerSerializer, \
    ProductUkDetailWholesalerSerializer, ProductRuDetailWholesalerSerializer, ProductDetailWholesalerSerializer, \
    ProductDetailRetailWholesalerSerializer, ProductDetailDropshipperSerializer
from users.permissions import IsEditorUser
from .models import Product


class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializers
    permission_classes = [IsEditorUser]


class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name_product', 'article', 'name_product_uk', 'name_product_ru']
    filterset_class = PriceFilter
    pagination_by = 25
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser) or self.request.user.role == 3:
            if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return ProductUkListCustomerSerializer
            elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return ProductRuListCustomerSerializer
            return ProductListCustomerSerializer
        else:
            if self.request.user.role == 2:
                return ProductListSerializer
            if self.request.user.role == 4:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return ProductUkListWholesalerSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return ProductRuListWholesalerSerializer
                return ProductListWholesalerSerializer
            if self.request.user.role == 5:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return ProductUkListRetailWholesalerSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return ProductRuListRetailWholesalerSerializer
                return ProductListRetailWholesalerSerializer
            if self.request.user.role == 6:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return ProductUkListDropshipperSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return ProductRuListDropshipperSerializer
                return ProductListDropshipperSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Product.objects.annotate(middle_star=Round(Avg('rating__star')))
    lookup_field = 'slug'

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser) or self.request.user.role == 3:
            if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return ProductUkDetailCustomerSerializers
            elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return ProductRuDetailCustomerSerializers
            return ProductDetailCustomerSerializers
        else:
            if self.request.user.role == 2:
                return ProductDetailSerializers
            if self.request.user.role == 4:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return ProductUkDetailWholesalerSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return ProductRuDetailWholesalerSerializer
                return ProductDetailWholesalerSerializer
            if self.request.user.role == 5:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return ProductUkDetailRetailWholesalerSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return ProductRuDetailRetailWholesalerSerializer
                return ProductDetailRetailWholesalerSerializer
            if self.request.user.role == 6:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return ProductUkDetailDropshipperSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return ProductRuDetailDropshipperSerializer
                return ProductDetailDropshipperSerializer

    permission_classes = [IsEditorUser, ]
