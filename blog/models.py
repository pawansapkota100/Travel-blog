from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


# Create your models here.

class Tag(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title= models.CharField(max_length=150,verbose_name="Title of blog post")
    content= CKEditor5Field('Text', config_name='default')
    tag= models.ManyToManyField(Tag)
    image = CloudinaryField('blog')
    slug = models.SlugField(unique=True, editable=False)
    created_at= models.DateField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Generate a unique slug
        if not self.slug:
            self.slug = slugify(self.title)
            # Ensure uniqueness
            while Blog.objects.filter(slug=self.slug).exists():
                self.slug = f"{self.slug}-{self.pk}" if self.pk else f"{self.slug}-1"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Comment(models.Model):
    full_name= models.CharField(max_length=50,default='')
    email= models.EmailField()
    website= models.CharField(max_length=50, null=True, blank=True)
    comment= models.TextField()
    blog= models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    parent= models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.comment
    

class Contact(models.Model):
    name= models.CharField(max_length=50)
    image= CloudinaryField('Contact', null=True, blank=True)
    description= CKEditor5Field('Text', config_name='default', null=True, blank=True)
    email= models.EmailField()
    phone_number= models.CharField(max_length=50, null=True, blank=True)
    message= models.TextField()
    created_at= models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Gallery(models.Model):
    title= models.CharField(max_length=50)
    image = CloudinaryField('Gallery')
    description= models.TextField()
    alt= models.CharField(max_length=50)
    created_at= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class AboutUs(models.Model):
    title= models.CharField(max_length=50)
    description= CKEditor5Field('Text', config_name='default')
    image= CloudinaryField('AboutUs')
    created_at= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class whosme(models.Model):
    title= models.CharField(max_length=50)
    description= CKEditor5Field('Text', config_name='default')
    image= CloudinaryField('whosme')
    phone= models.CharField(max_length=50)
    email= models.EmailField()
    created_at= models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

class ClientMessage(models.Model):
    name= models.CharField(max_length=50)
    email= models.EmailField()
    message= models.TextField()
    created_at= models.DateField(auto_now_add=True)

class Carousel(models.Model):
    title= models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    image= CloudinaryField('Carousel')

class FlickrFeed(models.Model):
    title= models.CharField(max_length=50)
    image= CloudinaryField('FlickrFeed')

