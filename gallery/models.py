from django.db import models

# Create your models here.
class Image(models.Model):
    picha_name = models.CharField(max_length =30)
    description = models.CharField(max_length =100)

class Location(models.Model):
    place = models.CharField(max_length =30)

class Category(models.Model):
    cat_name = models.CharField(max_length =30)
    