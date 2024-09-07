# FILE: /blog_project/djangoapp/site_setup/models.py

from django.db import models

# LOCALE⬇: http://127.0.0.1:8000/admin/site_setup/menulink/
class MenuLink(models.Model):
    # COMMENT⬇: Set metadata options.
    class Meta:
        # LOCALE⬇: http://127.0.0.1:8000/admin/site_setup/menulink/
        verbose_name = 'Menu Links'
        verbose_name_plural = 'Menu Links'

    # LOCALE⬇: http://127.0.0.1:8000/admin/site_setup/menulink/add/
    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)

    # COMMENT⬇: Before: class SiteSetup(models.Model).
    # COMMENT2⬇: 'Sitesetup' can have multiple 'MenuLinks'. Otherwise it cannot.
    # COMMENT3⬇: class SiteSetup(models.Model).
    # POINT⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/add/
    site_setup = models.ForeignKey('SiteSetup', on_delete=models.CASCADE, blank=True, null=True, default=None,)

    # COMMENT⬇: String representation.
    def __str__(self):
        return self.text

# LOCALE⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/
class SiteSetup(models.Model):
    # COMMENT⬇: Set metadata options.
    class Meta:
        # LOCALE⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/
        verbose_name = 'Setup'
        verbose_name_plural = 'Setup'
    
    # LOCALE⬇: http://127.0.0.1:8000/admin/site_setup/sitesetup/add/
    # COMMENT⬇: Website title.
    title = models.CharField(max_length=65)
    # COMMENT⬇: Description field.
    description = models.CharField(max_length=255)

    # COMMENT⬇: Visible fields and if selected marked.
    # VISIBLE⬇: They will be visible on the website.
    show_header = models.BooleanField(default=True)
    show_search = models.BooleanField(default=True)
    show_menu = models.BooleanField(default=True)
    show_description = models.BooleanField(default=True)
    show_pagination = models.BooleanField(default=True)
    show_footer = models.BooleanField(default=True)

    # COMMENT⬇: Website favicon image.
    favicon = models.ImageField(upload_to='assets/favicon/%Y/%m/', blank=True, default='') #1: ##

    def __str__(self):
        return self.title
    
    
#1: Estamos definindo onde as imagens serão armazenadas e de que forma (na pasta teremos o ano e mês). Ela ainda poderá enviar sem a imagem e se for assim o valor padrão será uma string.