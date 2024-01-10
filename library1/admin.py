from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Description', 'Author', 'count']
    list_filter = ['Author', 'Description']
    list_per_page = 10
    
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['ISBN','collection', 'is_taken']
    list_editable = ['is_taken']
    list_per_page = 10

@admin.register(Order)
class BookAdmin(admin.ModelAdmin):
    list_display = ['user','collection', 'book', 'date_taken', 'date_to_return']
    # list_filter = []
    list_per_page = 10


@admin.register(Returned)
class BookAdmin(admin.ModelAdmin):
    list_display = ['user','order', 'date_returned']
    # list_filter = []
    list_per_page = 10