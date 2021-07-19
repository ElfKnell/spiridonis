from django.contrib.auth.models import AnonymousUser
from django.db.models import Avg
from django.db.models.functions import Round
from django.shortcuts import render
from rest_framework import generics

from product.models import Product
from .serializers import CategorySerializer, CategoryDetailSerializer, CategoryListSerializer, \
    CategoryCustomerDetailSerializer, CategoryWholesalerDetailSerializer, \
    CategoryRetailWholesalerDetailSerializer, CategoryDropshipperDetailSerializer
from .models import Category
from users.permissions import IsEditorUser


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsEditorUser]


class CategoryListView(generics.ListAPIView):
    serializer_class = CategoryListSerializer
    queryset = Category.objects.all()


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Category.objects.all()
    permission_classes = [IsEditorUser]

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser):
            return CategoryCustomerDetailSerializer
        else:
            if self.request.user.role == 2:
                return CategoryDetailSerializer
            if self.request.user.role == 3:
                return CategoryCustomerDetailSerializer
            if self.request.user.role == 4:
                return CategoryWholesalerDetailSerializer
            if self.request.user.role == 5:
                return CategoryRetailWholesalerDetailSerializer
            if self.request.user.role == 6:
                return CategoryDropshipperDetailSerializer
