from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.image = Image(image = 'derro',image_name = 'beach',description = 'along the beach',location = 'kwale',category = 'sport')