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
    
    
#--------------Products Slider Model--------------#
class ProductsSliderCreateView(generics.ListCreateAPIView):
    queryset = ProductSliderModel.objects.all()
    serializer_class = ProductSliderSerializers

class ProductSliderReadView(generics.ListAPIView):
    queryset = ProductSliderModel.objects.all()
    serializer_class = ProductSliderSerializers

class ProductSliderUpdateView(generics.RetrieveUpdateAPIView):
    queryset = ProductSliderModel.objects.all()
    serializer_class = ProductSliderSerializers

class ProductSliderDeleteView(generics.DestroyAPIView):
    queryset = ProductSliderModel.objects.all()
    serializer_class = ProductSliderSerializers
    

#--------------User Model--------------#
class UserCreateView(generics.ListCreateAPIView):
    queryset = UsersModel.objects.all()
    serializer_class = UsersSerializers

class UserReadView(generics.ListAPIView):
    queryset = UsersModel.objects.all()
    serializer_class = UsersSerializers

class UserUpdateView(generics.RetrieveUpdateAPIView):
    queryset = UsersModel.objects.all()
    serializer_class = UsersSerializers

class UserDeleteView(generics.DestroyAPIView):
    queryset = UsersModel.objects.all()
    serializer_class = UsersSerializers
    
#--------------Profiles Model--------------#
class ProfileCreateView(generics.ListCreateAPIView):
    queryset = ProfilesModel.objects.all()
    serializer_class = UsersSerializers

class ProfileReadView(generics.ListAPIView):
    queryset = ProfilesModel.objects.all()
    serializer_class = ProfileSerializers

class ProfileUpdateView(generics.RetrieveUpdateAPIView):
    queryset = ProfilesModel.objects.all()
    serializer_class = ProfileSerializers

class ProfileDeleteView(generics.DestroyAPIView):
    queryset = ProfilesModel.objects.all()
    serializer_class = ProfileSerializers
    

#--------------WishList Model--------------#
class WishListCreateView(generics.ListCreateAPIView):
    queryset = WishListModel.objects.all()
    serializer_class = WishListSerializers

class WishListReadView(generics.ListAPIView):
    queryset = WishListModel.objects.all()
    serializer_class = WishListSerializers

class WishListUpdateView(generics.RetrieveUpdateAPIView):
    queryset = WishListModel.objects.all()
    serializer_class = WishListSerializers

class WishListDeleteView(generics.DestroyAPIView):
    queryset = WishListModel.objects.all()
    serializer_class = WishListSerializers


#--------------Cart Model--------------#
class CartCreateView(generics.ListCreateAPIView):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializers

class CartReadView(generics.ListAPIView):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializers

class CartUpdateView(generics.RetrieveUpdateAPIView):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializers

class CartDeleteView(generics.DestroyAPIView):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializers

#--------------Invoice Model--------------#
class InvoiceCreateView(generics.ListCreateAPIView):
    queryset = InvoiceModel.objects.all()
    serializer_class = InvoiceSerializers

class InvoiceReadView(generics.ListAPIView):
    queryset = InvoiceModel.objects.all()
    serializer_class = InvoiceSerializers

class InvoiceUpdateView(generics.RetrieveUpdateAPIView):
    queryset = InvoiceModel.objects.all()
    serializer_class = InvoiceSerializers

class InvoiceDeleteView(generics.DestroyAPIView):
    queryset = InvoiceModel.objects.all()
    serializer_class = InvoiceSerializers
    

#--------------Payment Model--------------#
class PaymentCreateView(generics.ListCreateAPIView):
    queryset = PaymentSettingsModel.objects.all()
    serializer_class = PaymentSerializers

class PaymentReadView(generics.ListAPIView):
    queryset = PaymentSettingsModel.objects.all()
    serializer_class = PaymentSerializers

class PaymentUpdateView(generics.RetrieveUpdateAPIView):
    queryset = PaymentSettingsModel.objects.all()
    serializer_class = PaymentSerializers

class PaymentDeleteView(generics.DestroyAPIView):
    queryset = PaymentSettingsModel.objects.all()
    serializer_class = PaymentSerializers
    

#--------------Features Model--------------#
class FeaturesCreateView(generics.ListCreateAPIView):
    queryset = FeaturesModel.objects.all()
    serializer_class = FeaturesSerializers

class FeaturesReadView(generics.ListAPIView):
    queryset = FeaturesModel.objects.all()
    serializer_class = FeaturesSerializers

class FeaturesUpdateView(generics.RetrieveUpdateAPIView):
    queryset = FeaturesModel.objects.all()
    serializer_class = FeaturesSerializers

class FeaturesDeleteView(generics.DestroyAPIView):
    queryset = FeaturesModel.objects.all()
    serializer_class = FeaturesSerializers
    

#----------------Product Details View--------------
class ProductDetailView(generics.ListAPIView):
    serializer_class = ProductsSerializers
    def get_queryset(self):
        id = self.kwargs['id']
        return ProductsModel.objects.filter(id=id)
    
#----------------Product By Category--------------
class ProductByCategoryView(generics.ListAPIView):
    serializer_class = ProductsSerializers
    def get_queryset(self):
        category_id = self.kwargs['category_ID']
        return ProductsModel.objects.filter(category_ID=category_id)
    
    
#----------Products by Brands-----------
class ProductsByBrandsView(generics.ListAPIView):
    serializer_class = ProductsSerializers
    def get_queryset(self):
        brand_id = self.kwargs['brand_ID']
        return ProductsModel.objects.filter(brand_ID = brand_id)