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
    

#--------------Product Model--------------#
class ProductCreateView(generics.ListCreateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializers

class ProductReadView(generics.ListAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializers

class ProductUpdateView(generics.RetrieveUpdateAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializers

class ProductDeleteView(generics.DestroyAPIView):
    queryset = ProductsModel.objects.all()
    serializer_class = ProductsSerializers
    
#--------------Products Details Model--------------#
class ProductsDetailsCreateView(generics.ListCreateAPIView):
    queryset = ProductsDetailsModel.objects.all()
    serializer_class = ProductsDetailsSerializers

class ProductDetailsReadView(generics.ListAPIView):
    queryset = ProductsDetailsModel.objects.all()
    serializer_class = ProductsDetailsSerializers

class ProductDetailsUpdateView(generics.RetrieveUpdateAPIView):
    queryset = ProductsDetailsModel.objects.all()
    serializer_class = ProductsDetailsSerializers

class ProductDetailsDeleteView(generics.DestroyAPIView):
    queryset = ProductsDetailsModel.objects.all()
    serializer_class = ProductsDetailsSerializers