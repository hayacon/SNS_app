from django.contrib import admin
from .models import *


class AppUserAdmin(admin.ModelAdmin):
    list_display=('user', 'profileImage', 'dateOfBirth', 'ocupation', 'organization', 'bio')


class PostAdmin(admin.ModelAdmin):
    list_display=('postId', 'userId', 'postDate', 'text', 'likes', 'media')

admin.site.register(AppUser, AppUserAdmin)
admin.site.register(Post, PostAdmin)
