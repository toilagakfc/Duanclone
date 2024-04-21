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

    