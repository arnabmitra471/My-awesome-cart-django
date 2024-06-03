from django.db import models

# Create your models here.
from base.models import BaseModel

class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug_field = models.SlugField(unique=True,null=True,blank=True)

    def __str__(self):
        return self.category_name

class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,related_name="products")
    slug_field = models.SlugField()
    price = models.IntegerField()
    product_description = models.TextField()
    product_image = models.ImageField(upload_to="products",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    feedback = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
