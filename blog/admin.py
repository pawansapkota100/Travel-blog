from django.contrib import admin
from .models  import Blog,Tag, Comment, Contact, Gallery,AboutUs, whosme,ClientMessage,Carousel,FlickrFeed
# Register your models here.

admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Gallery)
admin.site.register(AboutUs)
admin.site.register(whosme)
admin.site.register(Carousel)
admin.site.register(FlickrFeed)

class clientmessage(admin.ModelAdmin):
    list_display=['name','email','message']

    def __str__(self):
        return self.name


admin.site.register(ClientMessage,clientmessage)