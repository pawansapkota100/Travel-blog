# yourapp/context_processors.py

from .models import FlickrFeed

def flickr_feed(request):
    feeds = FlickrFeed.objects.all()  # Get all FlickrFeed objects
    return {'flickr_feeds': feeds}
