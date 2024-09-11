# FILE: /blog/project/djangoapp/blog/admin.py

from django.contrib import admin
from blog.models import Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ...




# https://linktr.ee/edsoncopque