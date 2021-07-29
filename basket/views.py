from django.contrib.auth.models import AnonymousUser
from django.db.models import F, Sum
from django.shortcuts import render
from rest_framework import generics, permissions

from basket.serializers import BasketSerializer, BasketCreateSerializer, BasketDetailCustomerSerializer, \
    OrderSerializer, \
    OrderDetailCustomerSerializer, SelectionSerializer, SelectionListSerializer, OrderDetailWholesalerSerializer, \
    OrderDetailRetailWholesalerSerializer, OrderDetailDropshipperSerializer, BasketDetailWholesalerSerializer, \
    BasketDetailRetailWholesalerSerializer, BasketDetailDropshipperSerializer, SelectionDetailSerializer
from users.permissions import IsEditorUser
from .models import Basket, Order, Selection
from .paginations import LargeResultsSetPagination


# Кошик
class BasketCreateView(generics.CreateAPIView):
    serializer_class = BasketCreateSerializer


class BasketListView(generics.ListAPIView):
    serializer_class = BasketSerializer
    queryset = Basket.objects.all()


class BasketDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Basket.objects.all()

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser):
            return BasketDetailCustomerSerializer
        else:
            if self.request.user.role == 3:
                return BasketDetailCustomerSerializer
            if self.request.user.role == 4:
                return BasketDetailWholesalerSerializer
            if self.request.user.role == 5:
                return BasketDetailRetailWholesalerSerializer
            if self.request.user.role == 6:
                return BasketDetailDropshipperSerializer


# Замовлення
class OrderCreateView(generics.CreateAPIView):

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser):
            return OrderDetailCustomerSerializer
        else:
            if self.request.user.role == 3:
                return OrderDetailCustomerSerializer
            if self.request.user.role == 4:
                return OrderDetailWholesalerSerializer
            if self.request.user.role == 5:
                return OrderDetailRetailWholesalerSerializer
            if self.request.user.role == 6:
                return OrderDetailDropshipperSerializer


class OrderListView(generics.ListAPIView):

    queryset = Order.objects.all()
    pagination_class = LargeResultsSetPagination
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Order.objects.all()
    permission_classes = [IsEditorUser, ]

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser):
            return OrderDetailCustomerSerializer
        else:
            if self.request.user.role == 2:
                return OrderSerializer
            if self.request.user.role == 3:
                return OrderDetailCustomerSerializer
            if self.request.user.role == 4:
                return OrderDetailWholesalerSerializer
            if self.request.user.role == 5:
                return OrderDetailRetailWholesalerSerializer
            if self.request.user.role == 6:
                return OrderDetailDropshipperSerializer


# Улюблені
class SelectionCreateView(generics.CreateAPIView):
    serializer_class = SelectionSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class SelectionListView(generics.ListAPIView):
    serializer_class = SelectionListSerializer
    queryset = Selection.objects.all()


class SelectionDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SelectionDetailSerializer
    queryset = Selection.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]

