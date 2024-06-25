from django.db import models

# Create your models here.
#Category Model
class CategoriesModel(models.Model):
    categoryName = models.CharField(max_length=255)
    categoryImg = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.categoryName

#Brands Model
class BrandsModel(models.Model):
    brandName = models.CharField(max_length=255)
    brandImg = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.categoryName
    
#Product Model
class ProductsModel(models.Model):
    title = models.CharField(max_length=255)
    shortDes = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    discount = models.BooleanField(default=False)
    discountPrice = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    star = models.CharField(max_length=255)
    stock = models.BooleanField(default=True)
    remark = models.CharField(max_length=255)
    categoryID = models.ForeignKey(CategoriesModel, on_delete= models.CASCADE)
    brandID = models.ForeignKey(BrandsModel, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)