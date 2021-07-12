from django.shortcuts import render
from rest_framework.response import Response

from .serializers import RatingSerializer, RatingStarSerializer, RatingListSerializer
from rest_framework.views import APIView
from rest_framework import generics
from .models import RatingStar, Rating
from .service import get_client_ip


class RatingStarCreateView(generics.CreateAPIView):
    serializer_class = RatingStarSerializer


class RatingStarListView(generics.ListAPIView):
    serializer_class = RatingStarSerializer
    queryset = RatingStar.objects.all()


class RatingStarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RatingStarSerializer
    queryset = RatingStar.objects.all()


class RatingCreateView(APIView):

    def post(self, request):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ip=get_client_ip(request))
            return Response(status=201)
        else:
            return Response(status=400)


class RatingListView(generics.ListAPIView):
    serializer_class = RatingListSerializer
    queryset = Rating.objects.all()
