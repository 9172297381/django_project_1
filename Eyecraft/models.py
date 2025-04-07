from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)  # ✅ Link to User model
    username = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.TextField(null=True,blank=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class Eyewear(models.Model):
    productId = models.AutoField(primary_key=True)
    productName = models.CharField(max_length=100)
    productPrice = models.DecimalField(max_digits=10, decimal_places=2)
    productDescription = models.TextField(null=True, blank=True)
    stockQuantity = models.PositiveIntegerField()

class EyewearDetails(models.Model):
    eyewear = models.OneToOneField(Eyewear, on_delete=models.PROTECT)
    brand = models.CharField(max_length=100)
    material = models.CharField(max_length=100)
    frameType = models.CharField(max_length=50, choices=[
        ('Full Rim', 'Full Rim'),
        ('Half Rim', 'Half Rim'),
        ('Rimless', 'Rimless'),
    ])
    lensType = models.CharField(max_length=50, choices=[
        ('Single Vision', 'Single Vision'),
        ('Bifocal', 'Bifocal'),
        ('Progressive', 'Progressive'),
        ('Blue Light', 'Blue Light'),
    ])
    warrantyPeriod = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.eyewear.productName} - {self.brand}"

from django.db import models

class LensProduct(models.Model):
    class CategoryChoices(models.TextChoices):
        EYE_GLASSES = "EYE_GLASSES", "Eye Glasses"
        POWER_GLASSES = "POWER_GLASSES", "Power Glasses"
        SUN_GLASSES = "SUN_GLASSES", "Sun Glasses"
        COMPUTER_GLASSES = "COMPUTER_GLASSES", "Computer Glasses"
        READING_GLASSES = "READING_GLASSES","Reading Glasses"
        CONTACT_LENSES = "CONTACT_LENSES", "Contact Lenses"
        ACCESSORIES = "ACCESSORIES", "Accessories"
        K_EYE_GLASSES = "k_EYE_GLASSES", "K_Eye Glasses"
        k_SUN_GLASSES = "k_SUN_GLASSES", "k_Sun Glasses"


    class RimTypeChoices(models.TextChoices):
        RIMMED = "RIMMED", "Rimmed"
        SEMI_RIMMED = "SEMI_RIMMED", "Semi-Rimmed"
        RIMLESS = "RIMLESS", "Rimless"

    productCategory = models.CharField(
        max_length=20,
        choices=CategoryChoices.choices,
        default=CategoryChoices.EYE_GLASSES
    )
    
    productRimType = models.CharField(
        max_length=20,
        choices=RimTypeChoices.choices,
        default=RimTypeChoices.RIMMED
    )


    BrandName = models.CharField(max_length=200, null=True, blank=True)  # Free text field for brand name
    productName = models.CharField(max_length=200)
    productDesc = models.TextField()
    productPrice = models.DecimalField(max_digits=7, decimal_places=2)

    productImage = models.ImageField(upload_to='images/')
    productImage_main = models.ImageField(upload_to='images/', null=True, blank=True)
    productImage_side = models.ImageField(upload_to='images/', blank=True, null=True)
    productImage_back = models.ImageField(upload_to='images/', blank=True, null=True)
    productImage_top = models.ImageField(upload_to='images/', blank=True, null=True)

    productRating = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)

    productCategory = models.CharField(
        max_length=50,
        choices=CategoryChoices.choices,
        default=CategoryChoices.EYE_GLASSES  # Default value
    )

    is_deleted = models.BooleanField(default=False)
    delete_details = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.productName} - {self.get_productCategory_display()}"
    

class cart(models.Model):
    uid=models.ForeignKey(User,on_delete=models.CASCADE,db_column='uid',null=True,blank=True)
    pid = models.ForeignKey(LensProduct, on_delete=models.CASCADE, db_column='pid',null=True,blank=True)
    qty = models.IntegerField(default=1)


class CustomerDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    custname = models.CharField(max_length=255)
    custEmail = models.EmailField()
    custAddress = models.TextField()
    custcontact = models.CharField(max_length=15)
    pincode = models.CharField(max_length=6)  # ✅ Must be CharField, NOT IntegerField!


    def __str__(self):
        return self.custname

from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100, unique=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(
        max_length=20, choices=[("Pending", "Pending"), ("Completed", "Completed")], default="Pending"
    )
    order_status = models.CharField(
        max_length=20, choices=[("Pending", "Pending"), ("Processing", "Processing"), ("Shipped", "Shipped"), ("Delivered", "Delivered")], default="Pending"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="order_items")
    product = models.ForeignKey(LensProduct, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.product.productName} (x{self.quantity})"

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="subcategories")
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.category.name} - {self.name}"

