from django.db import models
# Create your models here.

class Category (models.Model):
    
    categoryID = models.DecimalField(blank=False,null=False,max_digits=6,decimal_places=0)
    categoryName = models.CharField(max_length=100)
    parent = models.DecimalField(blank=True,null=True,max_digits=6,decimal_places=0) 
    image = models.CharField(max_length=255,null=False,blank=True)
    description = models.TextField(blank=True)
    STATUS_CATEGORY = [
    ("0", "Inactive"),
    ("1", "Active")
    ]
    status = models.CharField(max_length=20,choices=STATUS_CATEGORY,default='Inactive',blank=False,null=False)
    
    createdDate = models.DateTimeField(auto_now_add=True,editable=False)
    changeDate = models.DateTimeField(auto_now=True,blank=False)
    
class Atrribute(models.Model):
    attributesID = models.BigAutoField(max_digits=11,decimal_places=0,primary_key=True)
    attributeName = models.CharField(max_length=50,null=False,blank=False)

class AttributeValues(models.Model):
    attributesID = models.ForeignKey(Atrribute,to_field='attributesID')
    attributesValuesID = models.BigAutoField(max_digits=11,primary_key=True,decimal_places=0)
    attributesValues = models.CharField(max_length=100)

class Comments(models.Model):
    commentsID = models.BigAutoField(max_digits=11,primary_key=True)
    content = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    userID = models.DecimalField(max_digits=11)
    
class Products(models.Model):
    productID = models.BigAutoField(max_digits=11,primary_key=True)
    productName = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=11,decimal_places=0)
    promotionalPrice = models.DecimalField(max_digits=11,decimal_places=0,default=None)
    labelPromotion = models.CharField(max_length=10,default=None)
    description = models.TextField(default=None)
    brandProduct = models.CharField(max_length=100)
    codeProduct = models.CharField(max_length=50)
    typeName = models.CharField(max_length=50)
    STATUS_CATEGORY = [
    ("0", "Inactive"),
    ("1", "Active")
    ]
    status = models.CharField(max_length=20,choices=STATUS_CATEGORY,default='Inactive',blank=False,null=False)
    createdDate = models.DateTimeField(auto_now_add=True,editable=False)
    changeDate = models.DateTimeField(auto_now=True,blank=False)
    isHot = models.BooleanField(default=False)
    categoryID = models.DecimalField(blank=False,null=False,max_digits=6,decimal_places=0)