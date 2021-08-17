from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from rest_framework import generics
from rest_framework.filters import SearchFilter

from users.permissions import IsEditorUser
from .serializers import SetSerializer, SetListCustomerSerializer, SetListWholesalerSerializer, \
    SetListRetailWholesalerSerializer, SetListDropshipperSerializer, SetListSerializer, SetListUkCustomerSerializer, \
    SetListRuCustomerSerializer, SetListUkWholesalerSerializer, SetListRuWholesalerSerializer, \
    SetListUkRetailWholesalerSerializer, SetListRuRetailWholesalerSerializer, SetListUkDropshipperSerializer, \
    SetListRuDropshipperSerializer
from .models import Set


class SetCreateView(generics.CreateAPIView):
    serializer_class = SetSerializer
    permission_classes = [IsEditorUser]


class SetListView(generics.ListAPIView):
    pagination_by = 20
    filter_backends = [SearchFilter, ]
    search_fields = ['name_set', 'name_set_uk', 'name_set_ru']
    queryset = Set.objects.all()

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser) or self.request.user.role == 3:
            if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return SetListUkCustomerSerializer
            elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return SetListRuCustomerSerializer
            return SetListCustomerSerializer
        else:
            if self.request.user.role == 2:
                return SetListCustomerSerializer
            if self.request.user.role == 4:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return SetListUkWholesalerSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return SetListRuWholesalerSerializer
                return SetListWholesalerSerializer
            if self.request.user.role == 5:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return SetListUkRetailWholesalerSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return SetListRuRetailWholesalerSerializer
                return SetListRetailWholesalerSerializer
            if self.request.user.role == 6:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return SetListUkDropshipperSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return SetListRuDropshipperSerializer
                return SetListDropshipperSerializer


class SetDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Set.objects.all()
    permission_classes = [IsEditorUser, ]
    lookup_field = 'slug'

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser) or self.request.user.role == 3:
            if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return SetListUkCustomerSerializer
            elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return SetListRuCustomerSerializer
            return SetListCustomerSerializer
        else:
            if self.request.user.role == 2:
                return SetSerializer
            if self.request.user.role == 4:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return SetListUkWholesalerSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return SetListRuWholesalerSerializer
                return SetListWholesalerSerializer
            if self.request.user.role == 5:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return SetListUkRetailWholesalerSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return SetListRuRetailWholesalerSerializer
                return SetListRetailWholesalerSerializer
            if self.request.user.role == 6:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return SetListUkDropshipperSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return SetListRuDropshipperSerializer
                return SetListDropshipperSerializer
