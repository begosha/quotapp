from django.contrib import admin
from .models import Quote
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'author','email', 'rating', 'status','created_at', 'updated_at']
    list_filter = ['author']
    search_fields = ['text', 'author']
    fields = ['id', 'text', 'author','email', 'rating', 'status','created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at', 'id']

admin.site.register(Quote, QuoteAdmin)