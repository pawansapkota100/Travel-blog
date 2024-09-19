from django.db import models

# Create your models here.

class Tag(models.Model):
    name= models.CharField(max_length=50)

class Blog(models.Model):
    title= models.CharField(max_length=150,verbose_name="Title of blog post")
    content= models.TextField()
    tag= models.ManyToManyField(Tag)
    image= models.ImageField(upload_to="blog/")
    created_at= models.DateField(auto_now_add=True)