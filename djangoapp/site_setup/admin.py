# FILE: /blog_project/djangoapp/site_setup/admin.py

from django.contrib import admin
from site_setup.models import MenuLink, SiteSetup

@admin.register(MenuLink)
class MenuLinkAdmin(admin.ModelAdmin):
    
    # LOCALE: # /blog_project/djangoapp/site_setup/models.py
    list_display = 'id', 'text', 'url_or_path', 
    list_display_links = 'id', 'text', 'url_or_path',
    search_fields = 'id', 'text', 'url_or_path',

class MenuLinkInline(admin.TabularInline):
    
    # LOCALE: # /blog_project/djangoapp/site_setup/models.py
    model = MenuLink
    
    extra = 1

@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    
    # LOCALE: /blog_project/djangoapp/site_setup/models.py
    list_display = 'title', 'description',
    
    inlines = MenuLinkInline,

    def has_add_permission(self, request):

        # COMMENT: Just one.
        # return not SiteSetup.objects.exists()

        return True