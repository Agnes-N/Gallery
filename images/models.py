from django.db import models
import datetime as dt

# Create your models here.

class Image(models.Model):
    name = models.CharField(max_length =30)
    description = models.TextField()
    pic_image = models.ImageField(upload_to = 'images/', null=True)
    image_category = models.ForeignKey('Category', null=True)
    location = models.ForeignKey('Location', null=True)

    @classmethod
    def get_all_images(cls):
        images = cls.objects.all()
        return images

    def delete_image(self):
        self.delete()

    def save_image(self):
        self.save()

    @classmethod
    def update_image(cls,id,value):
        cls.objects.filter(id = id).update(pic_image = pic_image)

    @classmethod
    def get_image_by_id(cls,id):
        image = cls.objects.filter(id = id).all()
        return image

    @classmethod
    def search_by_category(cls,category_item):
        images = cls.objects.filter(image_category__category = category_item)
        return images

    @classmethod
    def filter_by_location(cls,id):
        images = cls.objects.filter(location__location = id)
        return images

    def __str__(self):
        return self.name

class Category(models.Model):
    categories = (("dogs","dogs"),("cats","cats"),("people","people"),("flowers","flowers")) 
    category = models.CharField(max_length = 255, choices = categories)

    class Meta: 
        verbose_name_plural = 'Category'
    def __str__(self):
        return f"{self.category}"

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls,id,new_category):
        cls.objects.filter(id = id).update(category = new_category)

class Location(models.Model):
    locations = (("UK","UK"),("RWANDA","RWANDA"),("CANADA","CANADA"),("USA","USA")) 
    location = models.CharField(max_length = 255, choices = locations)

    class Meta: 
        verbose_name_plural = 'Location'
    
    def save_location(self):
        self.save()

    @classmethod
    def get_location_id(cls,id):
        locate = cls.objects.get(id = id)
        return locate

    def __str__(self):
        return f"{self.location}"