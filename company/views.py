from django.shortcuts import render
from rest_framework import generics
from .serializers import CompanySerializer
from .models import Company
from users.permissions import IsEditorUser


class CompanyCreateView(generics.CreateAPIView):
    serializer_class = CompanySerializer
    permission_classes = [IsEditorUser, ]


class CompanyListView(generics.ListAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [IsEditorUser, ]


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
    permission_classes = [IsEditorUser, ]
