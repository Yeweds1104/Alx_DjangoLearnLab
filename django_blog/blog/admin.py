from django.contrib import admin
from .models import Comment

# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at', 'active')
    list_filter = ('active', 'created_at')
    search_fields = ('author__username', 'content')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
        
