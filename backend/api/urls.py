from . views import *
from django.urls import path

urlpatterns = [
    #--------------CategoriesModel--------------#
    path('categoties/create/', CategoriesCreateView.as_view(), name='Categories Create'),
    path('categoties/', CategoriesReadView.as_view(), name='Categories Read'),
    path('categoties/update/<int:pk>/', CategoriesUpdateView.as_view(), name='Categories Update'),
    path('categoties/delete/<int:pk>', CategoriesDeleteView.as_view(), name='Categories Delete'),
    
    #--------------Brands Model--------------#
    path('brands/create/', BrandCreateView.as_view(), name='Brands Create'),
    path('brands/', BrandReadView.as_view(), name='Brands Read'),
    path('brands/update/<int:pk>/', BrandUpdateView.as_view(), name='Brands Update'),
    path('brands/delete/<int:pk>', BrandDeleteView.as_view(), name='Brands Delete'),
    
    #--------------Products Model--------------#
    path('products/create/', ProductCreateView.as_view(), name='Brands Create'),
    path('products/', ProductReadView.as_view(), name='Brands Read'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='Brands Update'),
    path('products/delete/<int:pk>', ProductDeleteView.as_view(), name='Brands Delete'),
    
    
    #--------------Products Details Model--------------#
    path('products/details/create/', ProductsDetailsCreateView.as_view(), name='Brands Create'),
    path('products/details/', ProductDetailsReadView.as_view(), name='Brands Read'),
    path('products/details/update/<int:pk>/', ProductDetailsUpdateView.as_view(), name='Brands Update'),
    path('products/details/delete/<int:pk>', ProductDetailsDeleteView.as_view(), name='Brands Delete'),
]