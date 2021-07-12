from django.shortcuts import render
from rest_framework import generics
from .serializers import SetSerializer
from .models import Set


class SetCreateView(generics.CreateAPIView):
    serializer_class = SetSerializer
    permission_classes = []


class SetListView(generics.ListAPIView):
    serializer_class = SetSerializer
    queryset = Set.objects.all()
    permission_classes = []


class SetDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SetSerializer
    queryset = Set.objects.all()
    permission_classes = []
