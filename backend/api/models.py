from django.db import models

# Create your models here.
#Category Model
class CategoriesModel(models.Model):
    category_name = models.CharField(max_length=255)
    #category_img = models.CharField(max_length=255)
    category_img = models.ImageField(upload_to='images/categoryImg/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.category_name} - {self.category_img}"

#Brands Model
class BrandsModel(models.Model):
    brand_name = models.CharField(max_length=255)
    # brand_img = models.CharField(max_length=255)
    brand_img = models.ImageField(upload_to='images/brandImg/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.brand_name

class ProductRemarkModel(models.Model):
    remark_name = models.CharField(max_length=20)
    def __str__(self):
        return self.remark_name
    
#Product Model
class ProductsModel(models.Model):
    product_name = models.CharField(max_length=255)
    shortDes = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    discount = models.BooleanField(default=False)
    discountPrice = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/productImg/')
    star = models.CharField(max_length=255)
    stock = models.BooleanField(default=True)
    # remark = models.CharField(max_length=255)
    remark_ID = models.ForeignKey(ProductRemarkModel, on_delete= models.CASCADE)
    category_ID = models.ForeignKey(CategoriesModel, on_delete= models.CASCADE)
    brand_ID = models.ForeignKey(BrandsModel, on_delete= models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product_name

class ProductsDetailsModel(models.Model):
    img1 = models.ImageField(upload_to='images/productDetailImg/')
    img2 = models.ImageField(upload_to='images/productDetailImg/')
    img3 = models.ImageField(upload_to='images/productDetailImg/')
    #img1 = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    product_ID = models.ForeignKey(ProductsModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.description
    
class ProductSliderModel(models.Model):
    title = models.CharField(max_length=255)
    des = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/productSliderImg/')
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
    user_ID = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=255)
    customer_address = models.CharField(max_length=255)
    customer_city = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.customer_name
    
class WishListModel(models.Model):
    product_ID = models.ForeignKey(ProductsModel, on_delete=models.CASCADE)
    user_ID = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.productID.title

class CartModel(models.Model):
    product_ID = models.ForeignKey(ProductsModel, on_delete=models.CASCADE)
    user_ID = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    color = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    qty = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.productID.title
    
class InvoiceModel(models.Model):
    user_ID = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    payable = models.CharField(max_length=255)
    customer_details = models.CharField(max_length=255)
    shipping_details = models.CharField(max_length=255)
    trans_ID = models.CharField(max_length=255)
    val_ID = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)
    delivary_status = models.CharField(max_length=255)
    total = models.CharField(max_length=255)
    vat = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.userID.email

class InvoiceProductsModel(models.Model):
    product_ID = models.ForeignKey(ProductsModel, on_delete=models.CASCADE)
    invoice_ID = models.ForeignKey(InvoiceModel, on_delete=models.CASCADE)
    user_ID = models.ForeignKey(UsersModel, on_delete=models.CASCADE)
    color = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    qty = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.productID.title
    
class PaymentSettingsModel(models.Model):
    store_ID = models.CharField(max_length=255)
    store_Password = models.CharField(max_length=255)
    currency = models.CharField(max_length=255)
    success_URL = models.CharField(max_length=255)
    fail_URL = models.CharField(max_length=255)
    cancel_URL = models.CharField(max_length=255)
    ipn_URL = models.CharField(max_length=255)
    init_URL = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.store_ID

class FeaturesModel(models.Model):
    name = models.CharField(max_length=255)
    des = models.CharField(max_length=255)
    img = models.ImageField(upload_to='images/featureImg/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    
    def __str__(self):
        return self.name

