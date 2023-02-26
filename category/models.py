from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=100, unique=True)
    descriptions = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to='photos/categories', blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField(max_length=255, blank=True)
    image = models.ImageField(upload_to='photos/products', blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")

    def __str__(self):
        return self.name
    
class CustomUpload(models.Model):
    caption = models.CharField(max_length=200)
    SIZE_SELECT = (
        ('0','S'), 
        ('1','M'), 
        ('2','L')
    )
    size = models.CharField(max_length=11, choices=SIZE_SELECT)
    image = models.ImageField(upload_to='photos/custom')

    def __str__(self):
        return self.caption
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    