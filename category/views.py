from django.shortcuts import render
from rest_framework import generics
from .serializers import CategorySerializer, CategoryDetailSerializer
from .models import Category
from users.permissions import IsEditorUser


class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsEditorUser]


class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsEditorUser]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CategoryDetailSerializer
    queryset = Category.objects.all()
    permission_classes = [IsEditorUser]
