from django.shortcuts import render
from rest_framework import generics

from . models import *
from . serializers import *

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

#--------------Brand Model--------------#
class BrandCreateView(generics.ListCreateAPIView):
    queryset = BrandsModel.objects.all()
    serializer_class = BrandsSerializers

class BrandReadView(generics.ListAPIView):
    queryset = BrandsModel.objects.all()
    serializer_class = BrandsSerializers

class BrandUpdateView(generics.RetrieveUpdateAPIView):
    queryset = BrandsModel.objects.all()
    serializer_class = BrandsSerializers

class BrandDeleteView(generics.DestroyAPIView):
    queryset = BrandsModel.objects.all()
    serializer_class = BrandsSerializers