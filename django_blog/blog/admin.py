from django.contrib import admin
from .models import Comment, Tag, Post, Profile
from taggit.admin import TagAdmin, TaggedItemInline

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at', 'active')
    list_filter = ('active', 'created_at')
    search_fields = ('author__username', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
        
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [TaggedItemInline]
    list_display = ['title', 'author', 'published_date']
    filter_horizontal = ['tags']
