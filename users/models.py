from django.db import models
from django.contrib.auth.models import User
from PIL import Image

import cloudinary

from cloudinary.models import CloudinaryField
# Create your models here.

cloudinary.config( 
  secure=True,
  cloud_name = 'CLOUD_NAME', 
  api_key = 'API_KEY', 
  api_secret = 'API_SECRET' 
)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    bio = models.CharField(max_length=200, blank=True, null=True)
    profile_pic = CloudinaryField('profile_pics',default='media/default.png')
    is_teacher = models.BooleanField(default=False)
    website_url = models.CharField(max_length=255, blank=True, null=True)
    facebook_url = models.CharField(max_length=255, blank=True, null=True)
    instagram_url = models.CharField(max_length=255, blank=True, null=True)
    twitter_url = models.CharField(max_length=255, blank=True, null=True)
    linkedin_url = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username + ' Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.profile_pic.path)
        if img.height >100 or img.width>100:
            output_size = (100,100)
            img.thumbnail(output_size)
            img.save(self.profile_pic.path)

