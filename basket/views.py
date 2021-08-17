from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from rest_framework import generics, permissions

from basket.serializers import BasketSerializer, BasketCreateSerializer, BasketDetailCustomerSerializer, \
    OrderSerializer, \
    OrderDetailCustomerSerializer, SelectionSerializer, SelectionListSerializer, OrderDetailWholesalerSerializer, \
    OrderDetailRetailWholesalerSerializer, OrderDetailDropshipperSerializer, BasketDetailWholesalerSerializer, \
    BasketDetailRetailWholesalerSerializer, BasketDetailDropshipperSerializer, \
    OrderCreateSerializer, BasketDetailUkCustomerSerializer, BasketDetailRuCustomerSerializer, \
    BasketDetailRuDropshipperSerializer, BasketDetailUkDropshipperSerializer, BasketDetailRuRetailWholesalerSerializer, \
    BasketDetailUkRetailWholesalerSerializer, BasketDetailUkWholesalerSerializer, BasketDetailRuWholesalerSerializer, \
    SelectionListUkSerializer, SelectionListRuSerializer, OrderCreateUkSerializer, OrderCreateRuSerializer, \
    OrderDetailCustomerUkSerializer, OrderDetailCustomerRuSerializer, OrderDetailDropshipperUkSerializer, \
    OrderDetailDropshipperRuSerializer, OrderDetailRetailWholesalerRuSerializer, \
    OrderDetailRetailWholesalerUkSerializer, OrderDetailWholesalerRuSerializer, OrderDetailWholesalerUkSerializer
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
        if isinstance(self.request.user, AnonymousUser) or self.request.user.role == 3:
            if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return BasketDetailUkCustomerSerializer
            elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return BasketDetailRuCustomerSerializer
            return BasketDetailCustomerSerializer
        else:
            if self.request.user.role == 4:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return BasketDetailUkWholesalerSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return BasketDetailRuWholesalerSerializer
                return BasketDetailWholesalerSerializer
            if self.request.user.role == 5:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return BasketDetailUkRetailWholesalerSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return BasketDetailRuRetailWholesalerSerializer
                return BasketDetailRetailWholesalerSerializer
            if self.request.user.role == 6:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return BasketDetailUkDropshipperSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return BasketDetailRuDropshipperSerializer
                return BasketDetailDropshipperSerializer
# Кінець кошика


# Замовлення
class OrderCreateView(generics.CreateAPIView):
    #permission_classes = [permissions.IsAuthenticated, ]

    def get_serializer_class(self):
        if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return OrderCreateUkSerializer
        elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return OrderCreateRuSerializer
        return OrderCreateSerializer


class OrderListView(generics.ListAPIView):

    queryset = Order.objects.all()
    pagination_class = LargeResultsSetPagination
    serializer_class = OrderSerializer
    permission_classes = [IsEditorUser, ]


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Order.objects.all()
    permission_classes = [IsEditorUser, ]

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser) or self.request.user.role == 3:
            if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return OrderDetailCustomerUkSerializer
            elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return OrderDetailCustomerRuSerializer
            return OrderDetailCustomerSerializer
        else:
            if self.request.user.role == 2:
                return OrderSerializer
            if self.request.user.role == 4:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return OrderDetailWholesalerUkSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return OrderDetailWholesalerRuSerializer
                return OrderDetailWholesalerSerializer
            if self.request.user.role == 5:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return OrderDetailRetailWholesalerUkSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return OrderDetailRetailWholesalerRuSerializer
                return OrderDetailRetailWholesalerSerializer
            if self.request.user.role == 6:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return OrderDetailDropshipperUkSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return OrderDetailDropshipperRuSerializer
                return OrderDetailDropshipperSerializer
# Кінець замовлення


# Улюблені
class SelectionCreateView(generics.CreateAPIView):
    serializer_class = SelectionSerializer
    permission_classes = [permissions.IsAuthenticated, ]


class SelectionListView(generics.ListAPIView):
    queryset = Selection.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return SelectionListUkSerializer
        elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return SelectionListRuSerializer
        return SelectionListSerializer


class SelectionDetailView(generics.DestroyAPIView):
    serializer_class = SelectionSerializer
    queryset = Selection.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]

