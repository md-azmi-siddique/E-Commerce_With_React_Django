from django.conf import settings
from django.conf.urls.static import static
from . views import *
from django.urls import path

urlpatterns = [
    #--------------CategoriesModel--------------#
    path('categories/create/', CategoriesCreateView.as_view(), name='Categories Create'),
    path('categories/', CategoriesReadView.as_view(), name='Categories Read'),
    path('categories/update/<int:pk>/', CategoriesUpdateView.as_view(), name='Categories Update'),
    path('categories/delete/<int:pk>/', CategoriesDeleteView.as_view(), name='Categories Delete'),
    
    #--------------Brands Model--------------#
    path('brands/create/', BrandCreateView.as_view(), name='Brands Create'),
    path('brands/', BrandReadView.as_view(), name='Brands Read'),
    path('brands/update/<int:pk>/', BrandUpdateView.as_view(), name='Brands Update'),
    path('brands/delete/<int:pk>/', BrandDeleteView.as_view(), name='Brands Delete'),
    
    #--------------Product Remark Model--------------#
    
    path('remark/create/', ProductRemarkCreateView.as_view(), name='Brands Create'),
    path('remark/', ProductRemarkReadView.as_view(), name='Brands Read'),
    path('remark/update/<int:pk>/', ProductRemarkUpdateView.as_view(), name='Brands Update'),
    path('remark/delete/<int:pk>/', ProductRemarkDeleteView.as_view(), name='Brands Delete'),
    
    #--------------Products Model--------------#
    path('products/create/', ProductCreateView.as_view(), name='Brands Create'),
    path('products/', ProductReadView.as_view(), name='Brands Read'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='Brands Update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='Brands Delete'),
    
    
    #--------------Products Details Model--------------#
    path('products/details/create/', ProductsDetailsCreateView.as_view(), name='Brands Create'),
    path('products/details/', ProductDetailsReadView.as_view(), name='Brands Read'),
    path('products/details/update/<int:pk>/', ProductDetailsUpdateView.as_view(), name='Brands Update'),
    path('products/details/delete/<int:pk>/', ProductDetailsDeleteView.as_view(), name='Brands Delete'),

    #--------------Products Slider Model--------------#
    path('products/slider/create/', ProductsSliderCreateView.as_view(), name='Brands Create'),
    path('products/slider/', ProductSliderReadView.as_view(), name='Brands Read'),
    path('products/slider/update/<int:pk>/', ProductSliderUpdateView.as_view(), name='Brands Update'),
    path('products/slider/delete/<int:pk>/', ProductSliderDeleteView.as_view(), name='Brands Delete'),

    #--------------Users Model--------------#
    path('users/create/', UserCreateView.as_view(), name='Brands Create'),
    path('users/', UserReadView.as_view(), name='Brands Read'),
    path('users/update/<int:pk>/', UserUpdateView.as_view(), name='Brands Update'),
    path('users/delete/<int:pk>/', UserDeleteView.as_view(), name='Brands Delete'),

    #--------------profiles Model--------------#
    path('profiles/create/', ProfileCreateView.as_view(), name='Brands Create'),
    path('profiles/', ProfileReadView.as_view(), name='Brands Read'),
    path('profiles/update/<int:pk>/', ProfileUpdateView.as_view(), name='Brands Update'),
    path('profiles/delete/<int:pk>/', ProfileDeleteView.as_view(), name='Brands Delete'),

    #--------------product/wishlist Model--------------#
    path('product/wishlist/create/', WishListCreateView.as_view(), name='Brands Create'),
    path('product/wishlist/', WishListReadView.as_view(), name='Brands Read'),
    path('product/wishlist/update/<int:pk>/', WishListUpdateView.as_view(), name='Brands Update'),
    path('product/wishlist/delete/<int:pk>/', WishListDeleteView.as_view(), name='Brands Delete'),

    #--------------cart Model--------------#
    path('cart/create/', CartCreateView.as_view(), name='Brands Create'),
    path('cart/', CartReadView.as_view(), name='Brands Read'),
    path('cart/update/<int:pk>/', CartUpdateView.as_view(), name='Brands Update'),
    path('cart/delete/<int:pk>/', CartDeleteView.as_view(), name='Brands Delete'),

    #--------------invoice Model--------------#
    path('invoice/create/', InvoiceCreateView.as_view(), name='Brands Create'),
    path('invoice/', InvoiceReadView.as_view(), name='Brands Read'),
    path('invoice/update/<int:pk>/', InvoiceUpdateView.as_view(), name='Brands Update'),
    path('invoice/delete/<int:pk>/', InvoiceDeleteView.as_view(), name='Brands Delete'),

    #--------------payment Model--------------#
    path('payment/create/', PaymentCreateView.as_view(), name='Brands Create'),
    path('payment/', PaymentReadView.as_view(), name='Brands Read'),
    path('payment/update/<int:pk>/', PaymentUpdateView.as_view(), name='Brands Update'),
    path('payment/delete/<int:pk>/', PaymentDeleteView.as_view(), name='Brands Delete'),

    #--------------feature Model--------------#
    path('feature/create/', FeaturesCreateView.as_view(), name='Brands Create'),
    path('feature/', FeaturesReadView.as_view(), name='Brands Read'),
    path('feature/update/<int:pk>/', FeaturesUpdateView.as_view(), name='Brands Update'),
    path('feature/delete/<int:pk>/', FeaturesDeleteView.as_view(), name='Brands Delete'),
    
    #--------------Products By Cateegory-------#
    path('products/categories/<int:category_ID>/', ProductByCategoryView.as_view(), name='blogs-by-category'),
    
    #--------------Product Details--------------# 
    path('products/details/<int:id>/', ProductDetailView.as_view(), name='product-by-view'),
    
    #--------------Product By Brands--------------# 
    path('products/brands/<int:brand_ID>/', ProductsByBrandsView.as_view(), name='product-by-view'),
    
    #--------------Product By Remark--------------#
    path('products/remark/<int:remark_ID>/', ProductsByRemarkView.as_view(), name='product-by-view'),
]
