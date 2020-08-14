from django.contrib import admin
from blog.models import Post, BlogComment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ('title',)
    ordering = ('-date_posted',)


@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    ordering = ('-date_posted', )
