from django.contrib import admin
from .models import Blog, Comment, Contact, Gallery, AboutUs, whosme, ClientMessage, Carousel, FlickrFeed

class BlogAdmin(admin.ModelAdmin):
    actions = ['delete_all']

    @admin.action(description='Delete all records')
    def delete_all(self, request, queryset):
        queryset.delete()
        self.message_user(request, "All blog records have been deleted.")

class CommentAdmin(admin.ModelAdmin):
    actions = ['delete_all']

    @admin.action(description='Delete all records')
    def delete_all(self, request, queryset):
        queryset.delete()
        self.message_user(request, "All comment records have been deleted.")

class ContactAdmin(admin.ModelAdmin):
    actions = ['delete_all']

    @admin.action(description='Delete all records')
    def delete_all(self, request, queryset):
        queryset.delete()
        self.message_user(request, "All contact records have been deleted.")

class GalleryAdmin(admin.ModelAdmin):
    actions = ['delete_all']

    @admin.action(description='Delete all records')
    def delete_all(self, request, queryset):
        queryset.delete()
        self.message_user(request, "All gallery records have been deleted.")

class AboutUsAdmin(admin.ModelAdmin):
    actions = ['delete_all']

    @admin.action(description='Delete all records')
    def delete_all(self, request, queryset):
        queryset.delete()
        self.message_user(request, "All About Us records have been deleted.")

class WhosMeAdmin(admin.ModelAdmin):
    actions = ['delete_all']

    @admin.action(description='Delete all records')
    def delete_all(self, request, queryset):
        queryset.delete()
        self.message_user(request, "All Whos Me records have been deleted.")

class ClientMessageAdmin(admin.ModelAdmin):
    actions = ['delete_all']

    @admin.action(description='Delete all records')
    def delete_all(self, request, queryset):
        queryset.delete()
        self.message_user(request, "All client messages have been deleted.")

class CarouselAdmin(admin.ModelAdmin):
    actions = ['delete_all']

    @admin.action(description='Delete all records')
    def delete_all(self, request, queryset):
        queryset.delete()
        self.message_user(request, "All carousel records have been deleted.")

class FlickrFeedAdmin(admin.ModelAdmin):
    actions = ['delete_all']

    @admin.action(description='Delete all records')
    def delete_all(self, request, queryset):
        queryset.delete()
        self.message_user(request, "All Flickr feed records have been deleted.")

# Register your models with their corresponding admin classes
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(AboutUs, AboutUsAdmin)
admin.site.register(whosme, WhosMeAdmin)
admin.site.register(ClientMessage, ClientMessageAdmin)
admin.site.register(Carousel, CarouselAdmin)
admin.site.register(FlickrFeed, FlickrFeedAdmin)
