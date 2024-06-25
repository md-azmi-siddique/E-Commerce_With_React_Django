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
    
    def __str__(self):
        return self.title

class ProductsDetailsModel(models.Model):
    img1 = models.CharField(max_length=255)
    img2 = models.CharField(max_length=255)
    img3 = models.CharField(max_length=255)
    #img1 = models.CharField(max_length=255)
    des = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    productID = models.ForeignKey(ProductsModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.productID.title
    
class ProductSliderModel(models.Model):
    title = models.CharField(max_length=255)
    des = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    img = models.CharField(max_length=255)
    productID = models.ForeignKey(ProductsModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.title
    
class UsersModel(models.Model):
    email = models.CharField(max_length=355)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.email

class ProfilesModel(models.Model):
    userID = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    customer_address = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=255)
    customer_name = models.CharField(max_length=255)
    customer_city = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.customer_name
    
class WishListModel(models.Model):
    productID = models.ForeignKey(ProductsModel, on_delete=models.CASCADE)
    userID = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.productID.title