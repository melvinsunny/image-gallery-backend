from django.contrib import admin
from .models import *

# Register your models here.
class ImageDetailAdmin(admin.ModelAdmin):
    pass
admin.site.register(ImageDetail, ImageDetailAdmin)