from rest_framework import serializers

from .models import CategoriesModel, BrandsModel

class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoriesModel
        fields = '__all__'

class BrandsSerializers(serializers.ModelSerializer):
    class Meta:
        model = BrandsModel
        fields = '__all__'