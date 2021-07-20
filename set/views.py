from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from rest_framework import generics

from users.permissions import IsEditorUser
from .serializers import SetSerializer, SetListCustomerSerializer, SetListWholesalerSerializer, \
    SetListRetailWholesalerSerializer, SetListDropshipperSerializer, SetListSerializer
from .models import Set


class SetCreateView(generics.CreateAPIView):
    serializer_class = SetSerializer
    permission_classes = [IsEditorUser]


class SetListView(generics.ListAPIView):

    queryset = Set.objects.all()

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser):
            return SetListCustomerSerializer
        else:
            if self.request.user.role == 2:
                return SetListSerializer
            if self.request.user.role == 3:
                return SetListCustomerSerializer
            if self.request.user.role == 4:
                return SetListWholesalerSerializer
            if self.request.user.role == 5:
                return SetListRetailWholesalerSerializer
            if self.request.user.role == 6:
                return SetListDropshipperSerializer


class SetDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Set.objects.all()
    permission_classes = [IsEditorUser, ]

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser):
            return SetListCustomerSerializer
        else:
            if self.request.user.role == 2:
                return SetSerializer
            if self.request.user.role == 3:
                return SetListCustomerSerializer
            if self.request.user.role == 4:
                return SetListWholesalerSerializer
            if self.request.user.role == 5:
                return SetListRetailWholesalerSerializer
            if self.request.user.role == 6:
                return SetListDropshipperSerializer
