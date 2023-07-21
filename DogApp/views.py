from django.shortcuts import render

# Create your views here.
from .models import DogShop
from .serializer import ProductSerializer
from rest_framework import generics

class ProductList(generics.ListCreateAPIView):
    queryset = DogShop.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset =DogShop.objects.all()
    serializer_class = ProductSerializer