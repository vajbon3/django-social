from django.contrib import admin

from posts.models import Post, Photo

# Register your models here.
admin.site.register(Post)
admin.site.register(Photo)