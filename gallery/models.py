from django.db import models

# Create your models here.

class Location(models.Model):
    place = models.CharField(max_length =30)

    def __str__(self):
        return self.place

class Category(models.Model):
    cat_name = models.CharField(max_length =30)

    def __str__(self):
        return self.cat_name
    
class Image(models.Model):
    image = models.ImageField(upload_to = 'articles/', null = True)
    image_name = models.CharField(max_length =30)
    description = models.CharField(max_length =100)
    location = models.ForeignKey(Location , null = True)
    category = models.ManyToManyField(Category)
