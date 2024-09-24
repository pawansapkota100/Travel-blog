from typing import Any
from django.shortcuts import render,redirect
from django.views.generic import TemplateView,ListView,DetailView
from .forms import BlogForm, ContactForm,ContactUsForm
from .models import Blog,Gallery,AboutUs,whosme,Contact,Tag,Carousel
from django.core.paginator import Paginator

# Create your views here.

class HomeView(TemplateView):
    template_name = 'html/index.html'
    gallery = Gallery.objects.all()
    blog = Blog.objects.all()
    whosme = whosme.objects.first()

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        paginator = Paginator(self.blog, 5)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        # Add carousel items to the context
        carousel_items = Carousel.objects.all()

        context['gallery'] = self.gallery
        context['blogs'] = page_obj
        context['whosme'] = self.whosme
        context['carousel_items'] = carousel_items  # Add carousel to context
        context['form'] = ContactForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
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
        # context['contact_image'] = contact_info.image.url if contact_info.image else ''
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

        paginator=Paginator(Blog.objects.all(), 5)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['blogs'] =page_obj
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
    # def get_queryset(self):
    #  return Gallery.objects.all()  # Ensure this returns data

class GalleryView(TemplateView):
    template_name = 'html/gallery.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Get all gallery items
        gallery_items = Gallery.objects.all()
        
        # Create a Paginator object
        paginator = Paginator(gallery_items, 10)  # 2 items per page
        
        # Get the current page number from the request
        page_number = self.request.GET.get('page')
        
        # Get the items for the current page
        page_obj = paginator.get_page(page_number)

        context['gallery'] = page_obj
        return context