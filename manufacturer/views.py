from django.shortcuts import render
from .serializers import ManufacturerSerializer
from .models import Manufacturer
from users.permissions import IsEditorUser
from rest_framework import generics


class ManufacturerCreateView(generics.CreateAPIView):
    serializer_class = ManufacturerSerializer
    permission_classes = [IsEditorUser, ]


class ManufacturerListView(generics.ListAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()
    permission_classes = [IsEditorUser, ]


class ManufacturerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()
    permission_classes = [IsEditorUser, ]

