# FILE: /blog_project/djangoapp/site_setup/admin.py

from django.contrib import admin
from site_setup.models import MenuLink, SiteSetup

# IMPORT⬇: /blog_project/djangoapp/site_setup/models.py
@admin.register(MenuLink) #1: #10:
class MenuLinkAdmin(admin.ModelAdmin): #9:
    
    # EXPORT⬇: values to /blog_project/djangoapp/site_setup/models.py
    list_display = 'id', 'text', 'url_or_path', #2:
    list_display_links = 'id', 'text', 'url_or_path', #2:
    search_fields = 'id', 'text', 'url_or_path', #2:

class MenuLinkInline(admin.TabularInline): #3: #11:
    # URL⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/add/
    model = MenuLink #4: #12:
    extra = 3 #5:

# IMPORT⬇: /blog_project/djangoapp/site_setup/models.py
@admin.register(SiteSetup)
class SiteSetupAdmin(admin.ModelAdmin):
    
    # URL⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/
    # IMPORT⬇: /blog_project/djangoapp/site_setup/models.py
    list_display = 'title', 'description', #6:
    
    inlines = MenuLinkInline, #13:

    #URL⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/add/
    def has_add_permission(self, request): #14: #15:

        # return not SiteSetup.objects.exists() #8: #15:
        return True #7: #15:
    

# IMPORT, EXPORT and URL.

#1: Registering 'MenuLink' in Django.
#2: Fields displayed in Django Admin for the 'MenuLink' model defined in 'models.py'.
#3: 'Inline' to add/edit 'MenuLink' directly in 'SiteSetup' in Django Admin.
#4: Settings the 'MenuLink' template to be used as 'inline' in 'SiteSetup'.
#5: Number of extra entries displayer in the inline interface when adding a new object.
#6: Nomes apresentados como se fossem colunas. Define quais campos de 'SiteSetup' serão exibidos como colunas na lista de administração no Django Admin.
#7: Se 'return True', poderemos adicionar mais de um usuário em 'Setup'.
#8: Se este 'return' estiver ativado, vamos poder adicionar apenas um usuário.
#9: Esta classe é usada para personalizar como o modelo MenuLink será exibido e gerenciado na interface de administração do Django.
#10: É registrada com o decorador @admin.register(MenuLink) para que o Django Admin reconheça e utilize essa configuração ao lidar com o modelo MenuLink.
#11: Esta classe permite que objetos MenuLink sejam exibidos e editados diretamente na página de administração de outro modelo, SiteSetup, ao qual estão relacionados. Fornece uma interface inline para adicionar ou editar MenuLinks diretamente na página de administração de SiteSetup.
#12: Esta linha define que o modelo MenuLink será usado na classe MenuLinkInline como um modelo embutido (inline). Permite que o Django Admin saiba qual modelo está sendo usado para criar a interface inline. Garante que esses campos sejam visíveis e ordenáveis na interface de administração.
#13: Adiciona o 'MenuLinkInline' à página de administração de 'SiteSetup', permitindo que 'MenuLinks' relacionados sejam adicionados ou editados diretamente ali. Facilita a administração de objetos 'MenuLink' associados a 'SiteSetup'.
#14: Sobrescreve o método has_add_permission para controlar se um novo objeto SiteSetup pode ser adicionado no Django Admin.
#15:  Quando return True é utilizado, permite adicionar múltiplos registros de SiteSetup. Se o código comentado return not SiteSetup.objects.exists() for ativado, ele permitirá apenas um registro de SiteSetup.