from django.contrib import admin

from .models import Entry, Blog
# Register your models here.

admin.site.register(Entry)
admin.site.register(Blog)