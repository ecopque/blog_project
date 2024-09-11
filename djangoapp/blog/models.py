# FILE: /blog/project/djangoapp/blog/models.py

from django.db import models
from utils.rands import slugify_new


class Tag(models.Model): ##
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'

    name = models.CharField(max_length=15) ##
    slug = models.SlugField(unique=True, default=None, null=True, blank=True, max_length=255,) ##

    def save(self, *args, **kwargs):
        if not self.slug: #1: ##
            self.slug = slugify_new(self.name) ##
        return super().save(*args, **kwargs) ##





#1: Se a pessoa não tiver enviado uma slug, vou gerar uma nova 'slug'.

# https://linktr.ee/edsoncopque