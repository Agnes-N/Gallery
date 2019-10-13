from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class ImageTestClass(TestCase):
    
    # Setup method
    def setUp(self):
        self.location = Location(location='Africa')
        self.location.save()
        
        self.category = Category(category = 'fun')
        self.category.save()
        
        self.image = Image(pic_image = 'dog2.jpg', name='test',description='This is a test image',location = self.location, image_category = self.category)
        
        
    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    # Testing Instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))
        
    # testing the save method
    def test_save_method(self):
        self.image = Image(pic_image = 'dog2.jpg', name='test',description='This is a test image',location = self.location, image_category = self.category)
        self.image.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images) >= 1)
        
    def test_delete_method(self):
        self.image = Image(pic_image = 'dog2.jpg', name='test',description='This is a test image',location = self.location, image_category = self.category)
        self.image.save_image()
        images = self.image.delete_image()
        deleted = Image.objects.all()
        self.assertTrue(len(deleted) <= 0)
        
class LocationTestClass(TestCase):
    # SetUp Class
    def setUp(self):
        self.location = Location(location="UK")
        
    def tearDown(self):
        Location.objects.all().delete()
        
    def test_save_location(self):
        self.location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(location)>= 1)
        
        
