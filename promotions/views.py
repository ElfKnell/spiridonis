from django.contrib.auth.models import AnonymousUser

from users.permissions import IsEditorUser
from .models import Promotions
from .serializers import PromotionsSerializer, PromotionsUkListSerializer, PromotionsRuListSerializer, \
    PromotionsListSerializer, PromotionsUkDetailSerializer, PromotionsRuDetailSerializer, PromotionsDetailSerializer
from rest_framework import generics


class PromotionsCreateView(generics.CreateAPIView):
    serializer_class = PromotionsSerializer
    permission_classes = [IsEditorUser, ]


class PromotionsListView(generics.ListAPIView):
    queryset = Promotions.objects.all()

    def get_serializer_class(self):
        if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return PromotionsUkListSerializer
        elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
            return PromotionsRuListSerializer
        return PromotionsListSerializer


class PromotionsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promotions.objects.all()
    lookup_field = 'slug'
    permission_classes = [IsEditorUser, ]

    def get_serializer_class(self):
        if isinstance(self.request.user, AnonymousUser) or not self.request.user.role == 2:
            if 'uk' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return PromotionsUkDetailSerializer
            elif 'ru' in self.request.META.get('HTTP_ACCEPT_LANGUAGE'):
                return PromotionsRuDetailSerializer
            return PromotionsDetailSerializer
        else:
            return PromotionsSerializer
