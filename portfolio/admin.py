from django.contrib import admin
from .models import Project, BlogPost, Tag

admin.site.register(Project)
admin.site.register(BlogPost)
admin.site.register(Tag)
