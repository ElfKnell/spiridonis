from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .filters import UserFilter
from .serializers import AttributeValueSerializer, AttributeSerializer, \
    AttributeValueWholesalerListSerializer, AttributeValueRetailWholesalerListSerializer, \
    AttributeValueCustomerListSerializer, AttributeValueDropshipperListSerializer
from users.permissions import IsEditorUser
from .models import AttributesValue, Attributes


class AttributesValueCreateView(generics.CreateAPIView):
    serializer_class = AttributeValueSerializer
    #permission_classes = [IsEditorUser, ]


class AttributesCreateView(generics.CreateAPIView):
    serializer_class = AttributeSerializer
    #permission_classes = [IsEditorUser, ]


class AttributesValueListView(generics.ListAPIView):

    queryset = AttributesValue.objects.all()
    filter_backends = [DjangoFilterBackend, ]
    filter_class = UserFilter

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser):
            return AttributeValueCustomerListSerializer
        else:
            if self.request.user.role == 3:
                return AttributeValueCustomerListSerializer
            if self.request.user.role == 4:
                return AttributeValueWholesalerListSerializer
            if self.request.user.role == 5:
                return AttributeValueRetailWholesalerListSerializer
            if self.request.user.role == 6:
                return AttributeValueDropshipperListSerializer

    #permission_classes = [IsEditorUser, ]


class AttributesListView(generics.ListAPIView):
    serializer_class = AttributeSerializer
    queryset = Attributes.objects.all()
    #permission_classes = [IsEditorUser, ]


class AttributesValueDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AttributeValueSerializer
    queryset = AttributesValue.objects.all()
    #permission_classes = [IsEditorUser, ]


class AttributesDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AttributeSerializer
    queryset = Attributes.objects.all()
    #permission_classes = [IsEditorUser, ]

