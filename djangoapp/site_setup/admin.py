# /blog_project/djangoapp/site_setup/admin.py

from django.contrib import admin
from site_setup.models import MenuLink, SiteSetup ##

@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    list_display = 'id', 'text', 'url_or_path', # /blog_project/djangoapp/site_setup/models.py
    list_display_links = 'id', 'text', 'url_or_path', # /blog_project/djangoapp/site_setup/models.py
    search_fields = 'id', 'text', 'url_or_path', # /blog_project/djangoapp/site_setup/models.py

@admin.register(SiteSetup) ##
class SiteSetupAdmin(admin.ModelAdmin): ##
    list_display = 'title', 'description', # /blog_project/djangoapp/site_setup/models.py

    def has_add_permission(self, request): ##
        return not SiteSetup.objects.exists() #5: #6: ##