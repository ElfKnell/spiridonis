from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics

from .filters import UserFilter
from .serializers import AttributeValueSerializer, AttributeSerializer, AttributeVariantSerializer, \
    AttributeValueListSerializer
from users.permissions import IsEditorUser
from .models import AttributesValue, Attributes, AttributeVariant


class AttributesValueCreateView(generics.CreateAPIView):
    serializer_class = AttributeValueSerializer
    #permission_classes = [IsEditorUser, ]


class AttributesCreateView(generics.CreateAPIView):
    serializer_class = AttributeSerializer
    #permission_classes = [IsEditorUser, ]


class AttributesVariantCreateView(generics.CreateAPIView):
    serializer_class = AttributeVariantSerializer
    #permission_classes = [IsEditorUser, ]




class AttributesValueListView(generics.ListAPIView):
    serializer_class = AttributeValueListSerializer
    queryset = AttributesValue.objects.all()
    filter_backends = [DjangoFilterBackend, ]
    filter_class = UserFilter
    #permission_classes = [IsEditorUser, ]


class AttributesListView(generics.ListAPIView):
    serializer_class = AttributeSerializer
    queryset = Attributes.objects.all()
    #permission_classes = [IsEditorUser, ]


class AttributesVariantListView(generics.ListAPIView):
    serializer_class = AttributeVariantSerializer
    queryset = AttributeVariant.objects.all()
    #permission_classes = [IsEditorUser, ]


class AttributesValueDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AttributeValueSerializer
    queryset = AttributesValue.objects.all()
    #permission_classes = [IsEditorUser, ]


class AttributesDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AttributeSerializer
    queryset = Attributes.objects.all()
    #permission_classes = [IsEditorUser, ]


class AttributesVariantDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AttributeVariantSerializer
    queryset = AttributeVariant.objects.all()
    #permission_classes = [IsEditorUser, ]
