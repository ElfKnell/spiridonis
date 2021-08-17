from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from rest_framework import generics
from .serializers import NewsSerializer, NewsListSerializer, NewsRuListSerializer, NewsUkListSerializer, \
    NewsUkDetailSerializer, NewsRuDetailSerializer, NewsEnDetailSerializer, NewsDetailSerializer
from users.permissions import IsEditorUser
from .models import News


class NewsCreateView(generics.CreateAPIView):
    serializer_class = NewsSerializer
    #permission_classes = [IsEditorUser, ]


class NewsListView(generics.ListAPIView):

    queryset = News.objects.all()

    def get_serializer_class(self):

        if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return NewsUkListSerializer
        elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return NewsRuListSerializer
        return NewsListSerializer


class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = News.objects.all()
    lookup_field = 'part_link'
    permission_classes = [IsEditorUser, ]

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser) or not self.request.user.role == 2:
            if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return NewsUkDetailSerializer
            elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return NewsRuDetailSerializer
            return NewsEnDetailSerializer
        else:
            return NewsDetailSerializer
