# FILE: /blog/project/djangoapp/blog/admin.py

from django.contrib import admin
from blog.models import Tag

# IMPORT⬇: /blog/project/djangoapp/blog/models.py
@admin.register(Tag) ##
class TagAdmin(admin.ModelAdmin): ##
    # URL⬇: http://127.0.0.1:8000/admin/blog/tag/
    list_display = 'id', 'name', 'slug', #2: ##
    list_display_links = 'id', 'name', ##
    search_fields = 'id', 'name', 'slug', ##
    list_per_page = 10 ##
    ordering = '-id', ##
    # URL⬇: http://127.0.0.1:8000/admin/blog/tag/add/
    prepopulated_fields = {"slug": ('name',),} #1:


#1: Significa que o campo "slug" vai pegar o valor deste outro campo 'name', ou seja, vai permitir na url (admin/blog/tag/add/) quando digitar uma nova tag automaticamente uma nova tag será reescrita.
#2: ID é default? 'name' e 'slug' são variáveis do 'models.py'?

# https://linktr.ee/edsoncopque