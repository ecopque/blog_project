# FILE: /blog/project/djangoapp/blog/admin.py

from django.contrib import admin
from blog.models import Tag

# IMPORT⬇: /blog/project/djangoapp/blog/models.py
# URL⬇: http://127.0.0.1:8000/admin/blog/tag/
@admin.register(Tag) ##
class TagAdmin(admin.ModelAdmin): ##
    list_display = 'id', 'name', 'slug', ##
    list_display_links = 'name', ##
    search_fields = 'id', 'name', 'slug', ##
    list_per_page = 10 ##
    ordering = '-id', ##
    prepopulated_fields = {"slug": ('name',),} #1:


#1: Significa que o campo "slug" vai pegar o valor deste outro campo 'name', ou seja, vai permitir na url (admin/blog/tag/add/) quando digitar uma nova tag automaticamente uma nova tag será reescrita.

# https://linktr.ee/edsoncopque