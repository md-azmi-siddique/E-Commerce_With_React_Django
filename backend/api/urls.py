from . views import *
from django.urls import path

urlpatterns = [
    #--------------CategoriesModel--------------#
    path('categoties/create/', CategoriesCreateView.as_view(), name='Categories Create'),
    path('categoties/', CategoriesReadView.as_view(), name='Categories Read'),
    path('categoties/update/<int:pk>/', CategoriesUpdateView.as_view(), name='Categories Update'),
    path('categoties/delete/<int:pk>', CategoriesDeleteView.as_view(), name='Categories Delete'),
]