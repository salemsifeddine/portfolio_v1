from django.contrib import admin
from .models import *

@admin.register(Description)
class AdminSlider(admin.ModelAdmin):
    list_display = ['title','status']
    search_fields = ['title' ,'status']
    date_hierarchy = 'created_at'
    prepopulated_fields = {"slug":("title",)}
    list_per_page = 3

admin.site.register(ContactUs)