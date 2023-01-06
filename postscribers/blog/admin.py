from django.contrib import admin
from .models import *
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','date')

admin.site.register(PostModel, PostAdmin)
admin.site.register(Comment)

