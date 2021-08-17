from django.contrib.auth.models import AnonymousUser
from rest_framework import generics

from .serializers import CategorySerializer, CategoryDetailSerializer, CategoryListSerializer, \
    CategoryCustomerDetailSerializer, CategoryWholesalerDetailSerializer, \
    CategoryRetailWholesalerDetailSerializer, CategoryDropshipperDetailSerializer, CategoryListUkSerializer, \
    CategoryListRUSerializer, CategoryCustomerUkDetailSerializer, CategoryCustomerRuDetailSerializer, \
    CategoryDropshipperRuDetailSerializer, CategoryDropshipperUkDetailSerializer, CategoryWholesalerUkDetailSerializer, \
    CategoryWholesalerRuDetailSerializer, CategoryRetailWholesalerUkDetailSerializer, \
    CategoryRetailWholesalerRuDetailSerializer
from .models import Category
from users.permissions import IsEditorUser


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsEditorUser]


class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return CategoryListUkSerializer
        elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return CategoryListRUSerializer
        return CategoryListSerializer


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    permission_classes = [IsEditorUser]
    lookup_field = 'slug'

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser) or self.request.user.role == 3:
            if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return CategoryCustomerUkDetailSerializer
            elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return CategoryCustomerRuDetailSerializer
            return CategoryCustomerDetailSerializer
        else:
            if self.request.user.role == 2:
                return CategoryDetailSerializer
            elif self.request.user.role == 4:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return CategoryWholesalerUkDetailSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return CategoryWholesalerRuDetailSerializer
                return CategoryWholesalerDetailSerializer
            elif self.request.user.role == 5:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return CategoryRetailWholesalerUkDetailSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return CategoryRetailWholesalerRuDetailSerializer
                return CategoryRetailWholesalerDetailSerializer
            elif self.request.user.role == 6:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return CategoryDropshipperUkDetailSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return CategoryDropshipperRuDetailSerializer
                return CategoryDropshipperDetailSerializer
