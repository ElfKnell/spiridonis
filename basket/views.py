from django.shortcuts import render
from rest_framework import generics, permissions

from basket.serializers import BasketSerializer, BasketCreateSerializer, BasketDetailSerializer, OrderSerializer, \
    OrderDetailSerializer, SelectionSerializer, SelectionListSerializer
from users.permissions import IsEditorUser
from .models import Basket, Order, Selection
from .paginations import LargeResultsSetPagination


class BasketCreateView(generics.CreateAPIView):
    serializer_class = BasketCreateSerializer


class BasketListView(generics.ListAPIView):
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()
    permission_classes = [IsEditorUser]


class BasketDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BasketDetailSerializer
    queryset = Basket.objects.all()


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer


class OrderListView(generics.ListAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()
    pagination_class = LargeResultsSetPagination


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = OrderDetailSerializer
    queryset = Order.objects.all()


class SelectionCreateView(generics.CreateAPIView):
    serializer_class = SelectionSerializer


class SelectionListView(generics.ListAPIView):
    serializer_class = SelectionListSerializer
    queryset = Selection.objects.all()


class SelectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SelectionSerializer
    queryset = Selection.objects.all()
    pagination_class = [permissions.IsAuthenticated, ]

