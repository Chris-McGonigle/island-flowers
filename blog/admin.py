from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'image',
        'created_on',
    )

    ordering = ('created_on',)

class CommentAdmin(admin.ModelAdmin):
    
    list_display = (
        'author',
        'post',
        'created',
    )

    list_filter = ('post', 'created')

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
