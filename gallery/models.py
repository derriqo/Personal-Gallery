from django.db import models

# Create your models here.

class Location(models.Model):
    place = models.CharField(max_length =30)

    def __str__(self):
        return self.place

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Category(models.Model):
    cat_name = models.CharField(max_length =30)

    def __str__(self):
        return self.cat_name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
    
class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/', null = True)
    image_name = models.CharField(max_length =30)
    description = models.CharField(max_length =100)
    location = models.ForeignKey(Location , null = True)
    img_category = models.ManyToManyField(Category)

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls,before,after):
        fetched_object=Image.objects.filter(image_name=before).update(image_name=after)
        return fetched_object


    @classmethod
    def search_by_category(cls,search_term):
        search_result = cls.objects.filter(img_category__cat_name__icontains=search_term)
        return search_result

    @classmethod
    def retrieve_all(cls):
        all_objects = Image.objects.all()
        for item in all_objects:
            return item

    @classmethod
    def get_image(cls):
        images=cls.objects.all()
        return images    


   
