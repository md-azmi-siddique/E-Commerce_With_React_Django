from django.shortcuts import render
from rest_framework import generics

from . models import CategoriesModel
from . serializers import CategoriesSerializers

# Create your views here.
#--------------CategoriesModel--------------#
class CategoriesCreateView(generics.ListCreateAPIView):
    queryset = CategoriesModel.objects.all()
    serializer_class = CategoriesSerializers

class CategoriesReadView(generics.ListAPIView):
    queryset = CategoriesModel.objects.all()
    serializer_class = CategoriesSerializers

class CategoriesUpdateView(generics.RetrieveUpdateAPIView):
    queryset = CategoriesModel.objects.all()
    serializer_class = CategoriesSerializers

class CategoriesDeleteView(generics.DestroyAPIView):
    queryset = CategoriesModel.objects.all()
    serializer_class = CategoriesSerializers
