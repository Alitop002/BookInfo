from django.contrib import admin
from .models import Books, Comments, Favorite,Category
from unfold.admin import ModelAdmin

@admin.register(Books)
class BookAdmin(ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author')
    list_display_links = ('title', 'author')
    list_filter = ('category', 'language')

@admin.register(Favorite)
class FavorAdmin(ModelAdmin):
    list_display = ('user', 'book')
    search_fields = ('user', 'book')
    list_display_links = ('user', 'book')

@admin.register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    list_display_links = ('name',)

@admin.register(Comments)
class CommAdmin(ModelAdmin):
    list_display = ('user', 'book')
    search_fields = ('user', 'book')
    list_display_links = ('user', 'book')


