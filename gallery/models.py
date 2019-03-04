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
    image = models.ImageField(upload_to = 'pictures/', null = True)
    image_name = models.CharField(max_length =30)
    description = models.CharField(max_length =100)
    location = models.ForeignKey(Location , null = True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.image_name

    @classmethod
    def get_image(cls):
        images=cls.objects.all()
        return images    