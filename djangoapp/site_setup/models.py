# FILE: /blog_project/djangoapp/site_setup/models.py

from django.db import models

# EXPORT⬇: /blog_project/djangoapp/site_setup/admin.py
# URL⬇: http://127.0.0.1:8000/admin/site_setup/menulink/
class MenuLink(models.Model): ##
    class Meta: #2:
        # URL⬇: http://127.0.0.1:8000/admin/site_setup/menulink/
        verbose_name = 'Menu Links'
        verbose_name_plural = 'Menu Links'

    # URL⬇: http://127.0.0.1:8000/admin/site_setup/menulink/add/
    # IMPORT⬇: values/var from /blog_project/djangoapp/site_setup/admin.py
    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False) #6:

    # URL3⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/add/
    site_setup = models.ForeignKey('SiteSetup', on_delete=models.CASCADE, blank=True, null=True, default=None,) #3: #4: ##

    def __str__(self): #7:
        return self.text

# URL⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/
# EXPORT⬇: /blog_project/djangoapp/site_setup/admin.py
class SiteSetup(models.Model): ##
    class Meta: #5:
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
    favicon = models.ImageField(upload_to='assets/favicon/%Y/%m/', blank=True, default='') #1: #11: ##

    def __str__(self):
        return self.title
    
    

# IMPORT, EXPORT and URL.

#1: Estamos definindo onde as imagens serão armazenadas e de que forma (na pasta teremos o ano e mês). Ela ainda poderá enviar sem a imagem e se for assim o valor padrão será uma string.
#2: Set metadata options.
#3: 'Sitesetup' can have multiple 'MenuLinks'. Otherwise it cannot.
#4: Is you delete the link from 'site_setup', it will delete all links.
#5: Set metadata options.
#6: Django default box.
#7: String representation.
#8: Website title.
#9: Description field.
#10: Visible fields and if selected marked on Django Admin.
#11: Website favicon image.