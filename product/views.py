from django.db.models import Q, Count
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

    def get_queryset(self, request):

        return Product.objects.all().annotate(
            rating_user=Count(Q("rating", filter=Q(rating__ip=get_client_ip(request))))
        )


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializers
    queryset = Product.objects.all()
    permission_classes = [IsEditorUser]

