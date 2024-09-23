from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from .forms import BlogForm
from .models import Blog,Gallery,AboutUs

# Create your views here.

class HomeView(TemplateView):
    template_name= 'html/index.html'
    

class AboutView(ListView):
    model=AboutUs
    template_name= 'html/about.html'
    context_object_name= 'about'

class ContactView(TemplateView):
    template_name= 'html/contact.html'

class BlogView(ListView):
    form_class=BlogForm
    model=Blog
    template_name= 'html/blog.html'
    context_object_name= 'blogs'

class BlogDetailsView(DetailView):
    model=Blog
    template_name= 'html/single.html'
    context_object_name= 'blog'
    

class GalleryView(ListView):
    model= Gallery
    template_name= 'html/gallery.html'
    context_object_name= 'gallery'