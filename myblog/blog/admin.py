from django.contrib import admin
from .models import Post, Comment, Category, Tag

'''@admin.register(Comment)'''
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'created_at', 'active')
    list_filter = ('active', 'created_at')
    search_fields = ('name', 'email', 'body')

admin.site.register(Category) 
admin.site.register(Tag) 
admin.site.register(Post) 
admin.site.register(Comment)
