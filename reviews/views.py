from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import ReviewsSerializers
from .models import Reviews


class ReviewsCreateView(generics.CreateAPIView):
    serializer_class = ReviewsSerializers
    #permission_classes = [IsAuthenticated, ]


class ReviewsListView(generics.ListAPIView):
    serializer_class = ReviewsSerializers
    queryset = Reviews.objects.all()
    permission_classes = [IsAuthenticated, ]


class ReviewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ReviewsSerializers
    queryset = Reviews.objects.all()
    permission_classes = [IsAuthenticated, ]
