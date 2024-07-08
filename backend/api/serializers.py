from rest_framework import serializers

from .models import *

class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoriesModel
        fields = '__all__'

class BrandsSerializers(serializers.ModelSerializer):
    class Meta:
        model = BrandsModel
        fields = '__all__'

class ProductRemarkSerializers(serializers.ModelSerializer):
    class Meta:
        model = ProductRemarkModel
        fields = '__all__'
        
class ProductsSerializers(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category_ID.category_name', read_only=True)
    brand_name = serializers.CharField(source = 'brand_ID.brand_name', read_only = True)
    remark_name = serializers.CharField(source = 'remark_ID.remark_name', read_only = True)
    class Meta:
        model = ProductsModel
        #fields = '__all__'
        fields = [
            'id',
            'product_name',
            'shortDes',
            'price',
            'discount',
            'discountPrice',
            'image',
            'star',
            'stock',
            'remark_name',
            
            'category_ID',
            'brand_ID',
            'remark_ID',
            'created_at',
            'updated_at',
            'brand_name',
            'category_name'
        ]


class ProductsDetailsSerializers(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product_ID.product_name', read_only=True)
    class Meta:
        model = ProductsDetailsModel
        #fields = '__all__'
        fields = ['id','img1', 'img2', 'img3', 'description', 'color', 'size', 'product_ID', 'product_name']

class ProductSliderSerializers(serializers.ModelSerializer):
    product_name = serializers.CharField(source = 'product_ID.product_name', read_only = True)
    class Meta:
        model = ProductSliderModel
        fields = ['id','title', 'des', 'price', 'img', 'productID', 'product_name']


class UsersSerializers(serializers.ModelSerializer):
    class Meta:
        model = UsersModel
        fields = '__all__'
        
        
class ProfileSerializers(serializers.ModelSerializer):
    user_email = serializers.CharField(source = 'user_ID.email', read_only = True)
    class Meta:
        model = ProfilesModel
        fields = '__all__'
        
class WishListSerializers(serializers.ModelSerializer):
    user_email = serializers.CharField(source = 'user_ID.email', read_only = True)
    product_name = serializers.CharField(source = 'product_ID.product_name', read_only = True)
    
    class Meta:
        model = WishListModel
        fields = '__all__'
        
class CartSerializers(serializers.ModelSerializer):
    user_email = serializers.CharField(source = 'user_ID.email', read_only = True)
    product_name = serializers.CharField(source = 'product_ID.product_name', read_only = True)
    class Meta:
        model = CartModel
        fields = '__all__'

class InvoiceSerializers(serializers.ModelSerializer):
    user_email = serializers.CharField(source = 'user_ID.email', read_only = True)
    #product_name = serializers.CharField(source = 'product_ID.product_name', read_only = True)   
    class Meta:
        model = InvoiceModel
        fields = '__all__'

class InvoiceProductSerializers(serializers.ModelSerializer):
    user_email = serializers.CharField(source = 'user_ID.email', read_only = True)
    product_name = serializers.CharField(source = 'product_ID.product_name', read_only = True)   
    customer_details = serializers.CharField(source = 'invoice_ID.customer_details', read_only = True)
    class Meta:
        model = InvoiceProductsModel
        fields = '__all__'

class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model = PaymentSettingsModel
        fields = '__all__'
        
class FeaturesSerializers(serializers.ModelSerializer):
    class Meta:
        model = FeaturesModel
        fields = '__all__'