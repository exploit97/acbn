from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
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
class Categorie(models.Model):
     name = models.CharField(max_length=255)

     def __str__(self):
        return self.name
    

class Post(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    #text = models.TextField()
    text = RichTextField(blank=True, null=True)
    post_image = CloudinaryField('image',default='media/blog.jpg')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now= True)
    categorie =models.ForeignKey(Categorie, on_delete = models.CASCADE, null=True, blank = True)
    likes = models.ManyToManyField(User, related_name ='blog_posts')
    snippet = models.CharField(max_length=255, default='Lire')

    def get_absolute_url(self):
        return reverse("blogs:post_detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    def total_likes(self):
        return self.likes.count()
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)


class Partner(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image = CloudinaryField('image',default='media/blog.jpg')
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now= True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("blogs:partners")

class Documents(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = RichTextField(blank=True, null=True)
    doc_file = models.FileField(upload_to='files/', blank=True,null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now= True)    

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blogs:documents")
    