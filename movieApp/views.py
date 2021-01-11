from django.shortcuts import render

from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView, RetrieveAPIView, RetrieveDestroyAPIView

from .models import Movies
from .serializer import MoviesSerializer

class MoviesList(ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer

class MovieDetails(RetrieveUpdateDestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MoviesSerializer