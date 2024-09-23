from typing import Any
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
from .forms import BlogForm, ContactForm,ContactUsForm
from .models import Blog,Gallery,AboutUs,whosme,Contact,Tag

# Create your views here.

class HomeView(TemplateView):
    template_name= 'html/index.html'
    gallery= Gallery.objects.all()
    blog= Blog.objects.all()
    whosme= whosme.objects.first()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        contex= super().get_context_data(**kwargs)
        contex['gallery']= self.gallery
        contex['blogs']= self.blog
        contex['whosme']= self.whosme
        contex['form']=  ContactForm()
        return contex
    
    def post(self, request, *args, **kwargs):
        form= ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context = self.get_context_data()
            context['form'] = form  
            return render(request, self.template_name, context)


    

class AboutView(ListView):
    model=AboutUs
    template_name= 'html/about.html'
    context_object_name= 'about'

class ContactView(TemplateView):
    template_name= 'html/contact.html'


    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context= super().get_context_data(**kwargs)
        contact_info = Contact.objects.first()  # Get the first contact entry
        context['contact_image'] = contact_info.image.url if contact_info.image else ''
        context['contact_description'] = contact_info.description
        context['form']= ContactUsForm()
        return context
    def post(self, request, *args, **kwargs):
        form= ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
        else:
            context = self.get_context_data()
            context['form'] = form
            return render(request, self.template_name, context)


class BlogView(TemplateView):
    template_name = 'html/blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['blogs'] = Blog.objects.all() 
        context['whosme']= whosme.objects.first()
        context['form'] = ContactForm()

        return context
    
    def post(self, request, *args, **kwargs):
        form=ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog')
        else:
            context = self.get_context_data()
            context['form'] = form
            return render(request, self.template_name, context)
class BlogDetailsView(DetailView):
    model=Blog
    template_name= 'html/single.html'
    context_object_name= 'blog'
    

class GalleryView(ListView):
    model= Gallery
    template_name= 'html/gallery.html'
    context_object_name= 'gallery'