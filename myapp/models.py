from django.db import models

# Create your models here.
class User(models.Model):
    fname=models.CharField(max_length=100)
    lname=models.CharField(max_length=100)
    email=models.EmailField()
    mobile=models.PositiveIntegerField()
    address=models.TextField()
    password=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to='profile_pic/',default='')
    usertype=models.CharField(max_length=100,default='buyer')

    def __str__(self):
        return self.fname+" "+self.lname

class Product(models.Model):
    seller=models.ForeignKey(User,on_delete=models.CASCADE)
    category=(
        ('Formal','Formal'),       
        ('Sports','Sports'),       
        ('Casual','Casual'),       
    )
    product_category=models.CharField(max_length=100,choices=category)
    brand=( 
        ('Skechers','Skechers'),
        ('Asics','Asics'),
        ('Adidas','Adidas'),
        ('Bata','Bata'),
    )
    product_brand=models.CharField(max_length=100,choices=brand)
    product_name=models.CharField(max_length=100)
    product_price=models.PositiveIntegerField()
    size=(
        ('7','7'),
        ('8','8'),
        ('9','9'),
        ('10','10'),
        ('11','11'),
    )
    product_size=models.CharField(max_length=100,choices=size)
    product_pic=models.ImageField(upload_to='profile_pic/')

    def __str__(self):
        return self.seller.fname+" - "+self.product_name
    
class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.user.fname+" - "+self.product.product_name

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    product_price=models.PositiveIntegerField()
    product_qty=models.PositiveIntegerField(default=1)
    total_price=models.PositiveIntegerField()
    payment_status=models.BooleanField(default=False)

    def __str__(self):
        return self.user.fname+" - "+self.product.product_name