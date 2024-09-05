# /blog_project/djangoapp/site_setup/models.py

from django.db import models

class MenuLink(models.Model):
    class Meta:
        verbose_name = 'Menu Link'
        verbose_name_plural = 'Menu Links'

    text = models.CharField(max_length=50)
    url_or_path = models.CharField(max_length=2048)
    new_tab = models.BooleanField(default=False)

    def __str__(self):
        return self.text

class SiteSetup(models.Model):
    class Meta:
        verbose_name = 'Setup'
        verbose_name_plural = 'Setups'

    title = models.CharField(max_length=65) #2: ##
    description = models.CharField(max_length=255) ##
    show_header = models.BooleanField(default=True) #3: ##
    show_search = models.BooleanField(default=True) #3:
    show_menu = models.BooleanField(default=True) #3:
    show_description = models.BooleanField(default=True) #3:
    show_pagination = models.BooleanField(default=True) #3:
    show_footer = models.BooleanField(default=True) #3: