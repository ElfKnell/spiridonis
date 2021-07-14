from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from rest_framework import generics
from .serializers import CompanySerializer, CompanyListSerializer
from .models import Company
from users.permissions import IsEditorUser


class CompanyCreateView(generics.CreateAPIView):
    serializer_class = CompanySerializer
    permission_classes = [IsEditorUser, ]


class CompanyListView(generics.ListAPIView):

    queryset = Company.objects.all()
    permission_classes = [IsEditorUser, ]

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser):
            return CompanyListSerializer
        if self.request.user.role == 2:
            return CompanySerializer
        else:
            return CompanyListSerializer


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Company.objects.all()
    permission_classes = [IsEditorUser, ]

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser):
            return CompanyListSerializer
        if self.request.user.role == 2:
            return CompanySerializer
        else:
            return CompanyListSerializer
