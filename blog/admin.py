from django.contrib import admin
from .models import Comment, Post
from .models import Category
# Register your models here.

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Comment )


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')
