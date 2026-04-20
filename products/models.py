from django.db import models
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(blank=True,null=True,unique=True)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args,**kwargs)

    def __str__(self):
        return self.name