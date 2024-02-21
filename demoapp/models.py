from django.db import models

# Create your models here.

class Category (models.Model):
    name=models.CharField(max_length=250, unique=True)
    slug=models.SlugField(max_length=250, unique=True)
    image=models.ImageField(upload_to='category', blank=True)
    desc=models.TextField(blank=True)
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def _str_(self):
        return '{}'.format(self.name)

class Product(models.Model):
    name=models.CharField(max_length=250, unique=True)
    slug=models.SlugField(max_length=250, unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE) 
    image=models.ImageField(upload_to='product',blank=True)
    desc=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'
    def _str_(self):
        return self.name