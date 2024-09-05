# /blog_project/djangoapp/site_setup/admin.py

from django.contrib import admin
from site_setup.models import MenuLink

@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = 'id', 'text', 'url_or_path', #6: ## # /blog_project/djangoapp/site_setup/models.py
    list_display_links = 'id', 'text', 'url_or_path', #7: ## # /blog_project/djangoapp/site_setup/models.py
    search_fields = 'id', 'text', 'url_or_path', #8: ## # /blog_project/djangoapp/site_setup/models.py