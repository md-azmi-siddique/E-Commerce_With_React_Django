from rest_framework import serializers

from .models import CategoriesModel

class CategoriesSerializers(serializers.ModelSerializer):
    class Meta:
        model = CategoriesModel
        fields = '__all__'