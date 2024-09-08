# FILE: /blog_project/djangoapp/site_setup/admin.py

from django.contrib import admin
from site_setup.models import MenuLink, SiteSetup

# IMPORT⬇: /blog_project/djangoapp/site_setup/models.py
@admin.register(MenuLink) #1:
class MenuLinkAdmin(admin.ModelAdmin): ##
    
    # EXPORT⬇: values to /blog_project/djangoapp/site_setup/models.py
    list_display = 'id', 'text', 'url_or_path', #2:
    list_display_links = 'id', 'text', 'url_or_path', #2:
    search_fields = 'id', 'text', 'url_or_path', #2:

class MenuLinkInline(admin.TabularInline): #3: ##
    # URL⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/add/
    model = MenuLink #4: ##
    extra = 3 #5:

# IMPORT⬇: /blog_project/djangoapp/site_setup/models.py
@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    
    # URL⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/
    # IMPORT⬇: /blog_project/djangoapp/site_setup/models.py
    list_display = 'title', 'description', #6: ##
    
    inlines = MenuLinkInline, ##

    #URL⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/add/
    def has_add_permission(self, request): ##

        # return not SiteSetup.objects.exists() #8:
        return True #7:
    

# IMPORT, EXPORT and URL.

#1: Registering 'MenuLink' in Django.
#2: Fields displayed in Django Admin for the 'MenuLink' model defined in 'models.py'.
#3: 'Inline' to add/edit 'MenuLink' directly in 'SiteSetup' in Django Admin.
#4: Settings the 'MenuLink' template to be used as 'inline' in 'SiteSetup'.
#5: Number of extra entries displayer in the inline interface when adding a new object.
#6: Nomes apresentados como se fossem colunas.
#7: Se 'return True', poderemos adicionar mais de um usuário em 'Setup'.
#8: Se este 'return' estiver ativado, vamos poder adicionar apenas um usuário.