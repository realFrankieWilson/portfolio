"""Amin registers models of of our applications."""
from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    """Displays the post's title, and the date on the admin page"""
    list_display = ('title', 'created_at')


# Register Your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
