from django.contrib import admin
from .models import Book, Comment

admin.site.register(Book)
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['book', 'user', 'text', 'datetime_created_at', 'is_active', 'recommend']
