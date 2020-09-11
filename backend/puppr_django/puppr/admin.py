from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import User, Post
# Register your models here.
admin.site.register(User)
admin.site.register(Post)
