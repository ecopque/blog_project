# FILE: /blog_project/djangoapp/site_setup/admin.py

from django.contrib import admin
from site_setup.models import MenuLink, SiteSetup

# IMPORT⬇: /blog_project/djangoapp/site_setup/models.py
@admin.register(MenuLink) #1: #10:
class MenuLinkAdmin(admin.ModelAdmin): #9:
    # EXPORT⬇: values to /blog_project/djangoapp/site_setup/models.py
    # URL⬇: http://127.0.0.1:8000/admin/site_setup/menulink/
    list_display = 'id', 'text', 'url_or_path', #2: #18:
    list_display_links = 'id', 'text', 'url_or_path', #16: #18:
    search_fields = 'id', 'text', 'url_or_path', #17:

class MenuLinkInline(admin.TabularInline): #11:
    # URL⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/add/
    model = MenuLink #12:
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
        # return not SiteSetup.objects.exists() #15:
        return True #15:
    

# IMPORT, EXPORT and URL.

#1: Registering 'MenuLink' in Django.
#2: Esta linha define os campos que serão exibidos na interface de administração do Django para o modelo 'MenuLink'. 'list_display' é uma propriedade de 'admin.ModelAdmin' que especifica quais campos de um modelo devem ser exibidos como **colunas** na lista de objetos na página de administração. Aqui, os campos 'id', 'text', e 'url_or_path' de 'MenuLink' serão exibidos.
#3: ???????????????????????????????????????????????????????????????????????????????
#4: ???????????????????????????????????????????????????????????????????????????????
#5: Number of extra entries displayer in the inline interface when adding a new object.
#6: Nomes apresentados como se fossem colunas. Define quais campos de 'SiteSetup' serão exibidos como colunas na lista de administração no Django Admin.
#7: ???????????????????????????????????????????????????????????????????????????????
#8: ???????????????????????????????????????????????????????????????????????????????
#9: Esta classe é usada para **personalizar** como o modelo 'MenuLink' será **exibido e gerenciado** na interface de administração do Django.
#10: É registrada com o decorador '@admin.register(MenuLink)' para que o Django Admin reconheça e utilize essa configuração ao lidar com o modelo 'MenuLink'.
#11: Esta classe permite que objetos 'MenuLink' sejam exibidos e editados diretamente na página de administração de outro modelo, 'SiteSetup', ao qual estão relacionados. Fornece uma interface inline para adicionar ou editar 'MenuLinks' diretamente na página de administração de 'SiteSetup'.
#12: Esta linha define que o modelo 'MenuLink' será usado na classe 'MenuLinkInline' como um modelo embutido (inline). Permite que o Django Admin saiba qual modelo está sendo usado para criar a interface inline. Garante que esses campos sejam visíveis e ordenáveis na interface de administração.
#13: Adiciona o 'MenuLinkInline' à página de administração de 'SiteSetup', permitindo que 'MenuLinks' relacionados sejam adicionados ou editados diretamente ali. Facilita a administração de objetos 'MenuLink' associados a 'SiteSetup'.
#14: Sobrescreve o método 'has_add_permission' para controlar se um novo objeto 'SiteSetup' pode ser adicionado no Django Admin.
#15:  Quando 'return True' é utilizado, permite adicionar múltiplos registros de 'SiteSetup'. Se o código comentado 'return not SiteSetup.objects.exists()' for ativado, ele permitirá apenas um registro de 'SiteSetup'.
#16: Este camada vai transformar os dados (das linhas abaixo) das colunas 'id', 'text' e 'url or path' em links, ou seja, pode clicar em cima que vai ser direcionado para o link específico. 
#17: Nesta linha vai ser mostrado o campo de pesquisa (Search) e os itens de busca são 'id', 'text' e 'url or path'.
#18: Estas duas linhas trabalham diretamente com '    text = models.CharField(max_length=50)' da classe 'MenuLink()' de 'models.py'. Fiz um teste e se mudar de 'text' para 'text2' e no 'MenuLink()' mudar a variável 'text' para 'text2' vai mudar o nome 'text' neste link: http://127.0.0.1:8000/admin/site_setup/menulink/add/.