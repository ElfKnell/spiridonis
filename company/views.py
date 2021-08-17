from django.contrib.auth.models import AnonymousUser
from rest_framework import generics
from .serializers import CompanySerializer, CompanyListSerializer, CompanyListUkSerializer, CompanyListRuSerializer
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
            if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return CompanyListUkSerializer
            elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return CompanyListRuSerializer
            return CompanyListSerializer
        if self.request.user.role == 2:
            return CompanySerializer
        else:
            if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return CompanyListUkSerializer
            elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return CompanyListRuSerializer
            return CompanyListSerializer


class CompanyDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Company.objects.all()
    permission_classes = [IsEditorUser, ]

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser):
            if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return CompanyListUkSerializer
            elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return CompanyListRuSerializer
            return CompanyListSerializer
        if self.request.user.role == 2:
            return CompanySerializer
        else:
            if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return CompanyListUkSerializer
            elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return CompanyListRuSerializer
            return CompanyListSerializer
