from django.contrib import admin

# Register your models here.

from .models import info, Image, Video

admin.site.register(info)
admin.site.register(Image)
admin.site.register(Video)
