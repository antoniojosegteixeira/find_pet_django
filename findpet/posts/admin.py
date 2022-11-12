from django.contrib import admin
from .models import Post, PostImage


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'created']
    list_filter = ['created']


admin.site.register(PostImage)
