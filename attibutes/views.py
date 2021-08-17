from django.contrib.auth.models import AnonymousUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .filters import UserFilter
from .serializers import AttributeValueSerializer, AttributeSerializer, \
    AttributeValueWholesalerListSerializer, AttributeValueRetailWholesalerListSerializer, \
    AttributeValueCustomerListSerializer, AttributeValueDropshipperListSerializer, \
    AttributeValueCustomerUkListSerializer, AttributeValueCustomerRuListSerializer, \
    AttributeValueRetailWholesalerUkListSerializer, AttributeValueRetailWholesalerRuListSerializer, \
    AttributeValueDropshipperRuListSerializer, AttributeValueDropshipperUkListSerializer, \
    AttributeValueWholesalerUkListSerializer, AttributeValueWholesalerRuListSerializer
from users.permissions import IsEditorUser
from .models import AttributesValue, Attributes


class AttributesValueCreateView(generics.CreateAPIView):
    serializer_class = AttributeValueSerializer
    permission_classes = [IsEditorUser, ]


class AttributesCreateView(generics.CreateAPIView):
    serializer_class = AttributeSerializer
    permission_classes = [IsEditorUser, ]


class AttributesValueListView(generics.ListAPIView):

    queryset = AttributesValue.objects.all()
    filter_backends = [DjangoFilterBackend, ]
    filter_class = UserFilter

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser) or self.request.user.role == 3:
            if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return AttributeValueCustomerUkListSerializer
            elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return AttributeValueCustomerRuListSerializer
            return AttributeValueCustomerListSerializer
        else:
            if self.request.user.role == 4:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return AttributeValueWholesalerUkListSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return AttributeValueWholesalerRuListSerializer
                return AttributeValueWholesalerListSerializer
            if self.request.user.role == 5:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return AttributeValueRetailWholesalerUkListSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return AttributeValueRetailWholesalerRuListSerializer
                return AttributeValueRetailWholesalerListSerializer
            if self.request.user.role == 6:
                if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return AttributeValueDropshipperUkListSerializer
                elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                    return AttributeValueDropshipperRuListSerializer
                return AttributeValueDropshipperListSerializer


class AttributesListView(generics.ListAPIView):
    serializer_class = AttributeSerializer
    queryset = Attributes.objects.all()
    permission_classes = [IsEditorUser, ]


class AttributesValueDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AttributeValueSerializer
    queryset = AttributesValue.objects.all()
    permission_classes = [IsEditorUser, ]


class AttributesDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AttributeSerializer
    queryset = Attributes.objects.all()
    permission_classes = [IsEditorUser, ]

