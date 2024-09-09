# FILE: /blog_project/djangoapp/site_setup/models.py

from django.db import models

# EXPORT⬇: /blog_project/djangoapp/site_setup/admin.py
# URL⬇: http://127.0.0.1:8000/admin/site_setup/menulink/
class MenuLink(models.Model): #12:
    class Meta: #2:
        # URL⬇: http://127.0.0.1:8000/admin/
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'
    # URL⬇: http://127.0.0.1:8000/admin/site_setup/menulink/add/
    # IMPORT⬇: values/var from /blog_project/djangoapp/site_setup/admin.py
    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False) #6:
    # URL3⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/add/
    site_setup = models.ForeignKey('SiteSetup', on_delete=models.CASCADE, blank=True, null=True, default=None,) #3: #4: #14:
    def __str__(self): #7:
        return self.text

# URL⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/
# EXPORT⬇: /blog_project/djangoapp/site_setup/admin.py
class SiteSetup(models.Model): #15:
    class Meta: #2:
        # URL⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/
        verbose_name = 'Setup'
        verbose_name_plural = 'Setup'
    
    # URL⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/add/
    title = models.CharField(max_length=65) #8:
    description = models.CharField(max_length=255) #9:
    show_header = models.BooleanField(default=True) #10:
    show_search = models.BooleanField(default=True) #10:
    show_menu = models.BooleanField(default=True) #10:
    show_description = models.BooleanField(default=True) #10:
    show_pagination = models.BooleanField(default=True) #10:
    show_footer = models.BooleanField(default=True) #10:

    # URL⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/add/
    # EXPORT⬇: /blog_project/data/web/media/assets/favicon/"year"/"month"
    favicon = models.ImageField(upload_to='assets/favicon/%Y/%m/', blank=True, default='') #17:

    def __str__(self):
        return self.title
    
#1: ???
#2: Os atributos 'verbose_name' e 'verbose_name_plural' definem como o modelo deve ser exibido na interface de administração do Django, no singular e no plural, respectivamente.
#3: 'Sitesetup' can have multiple 'MenuLinks'. Otherwise it cannot.
#4: Is you delete the link from 'site_setup', it will delete all links.
#5: ???
#6: Caixa de seleção do Django.
#7: String representation.
#8: Website title.
#9: Description field.
#10: Visible fields and if selected marked on Django Admin.
#11: ???
#12: Define a classe 'MenuLink', que herda de 'models.Model', tornando-a um modelo Django. Este modelo representa um link de menu na aplicação.
#13: ???
#14: Permite que vários 'MenuLinks' sejam associados a um único 'SiteSetup'. 'on_delete=models.CASCADE' garante que quando um 'SiteSetup' for excluído, todos os 'MenuLinks' relacionados também sejam excluídos.
#15: Define a classe 'SiteSetup', que herda de 'models.Model', tornando-a um modelo Django. Este modelo representa a configuração do site na aplicação.
#16: ???
#17: Permite o upload de um favicon, definindo onde as imagens serão armazenadas (upload_to) e permitindo que o campo seja opcional (blank=True) com um valor padrão de uma string vazia (default='').