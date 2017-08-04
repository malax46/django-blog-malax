from django.contrib import admin
from .models import Article, Category, Tag, Contact

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status','category')
    search_fields = ('title', 'body')
    raw_id_fields = ('user',)
    ordering = ['status'] 

class ContactAdmin(admin.ModelAdmin):
    list_display = ('contact_name', 'contact_email')
    search_fields = ('contact_name', 'content')

admin.site.register(Article,ArticleAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Contact, ContactAdmin)
