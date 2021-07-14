from django.shortcuts import render
from rest_framework import generics
from .serializers import NewsSerializer, NewsListSerializer
from users.permissions import IsEditorUser
from .models import News


class NewsCreateView(generics.CreateAPIView):
    serializer_class = NewsSerializer
    permission_classes = [IsEditorUser, ]


class NewsListView(generics.ListAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.all()


class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NewsListSerializer
    queryset = News.objects.all()
    permission_classes = [IsEditorUser, ]
