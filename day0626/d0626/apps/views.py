from django.shortcuts import render

from rest_framework import viewsets
from .models import Book,Game,Movie
from .serializers import BookSerializers,GameSerializers,MovieSerializers
from rest_framework.generics import CreateAPIView,ListAPIView,ListCreateAPIView


# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializers

# class MovieViewSet(CreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializers

# class MovieViewSet(ListAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializers

# class MovieViewSet(ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializers