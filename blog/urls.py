from django.urls import path
from .views import HomeView,AboutView, ContactView, BlogView, GalleryView,BlogDetailsView

urlpatterns = [
    path('',HomeView.as_view(),name='index'),
    path('about/',AboutView.as_view(),name='about'),
    path('gallery/',GalleryView.as_view(),name='gallery'),
    path('contact/',ContactView.as_view(),name='contact'),
    path('blog/',BlogView.as_view(),name='blog'),
    path('blog/<int:pk>/',BlogDetailsView.as_view(),name='blog_detail'),
]
