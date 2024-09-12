# FILE: /blog/project/djangoapp/blog/models.py

from django.db import models
from utils.rands import slugify_new

class Tag(models.Model):
    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
    #URL⬇: http://127.0.0.1:8000/admin/blog/tag/add/
    name = models.CharField(max_length=15) #2:
    slug = models.SlugField(unique=True, default=None, null=True, blank=True, max_length=255,) #3:
    def save(self, *args, **kwargs):
        if not self.slug: #1: #4:
            self.slug = slugify_new(self.name, 4) #5:
        return super().save(*args, **kwargs) #6:

class Category(models.Model): #7:
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=15)
    slug = models.SlugField(unique=True, default=None, null=True, blank=True, max_length=255,)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 4)
        return super().save(*args, **kwargs)

class Page(models.Model):
    title = models.CharField(max_length=65,) ##
    slug = models.SlugField(unique=True, default="", null=False, blank=True, max_length=255,) ##
    is_published = models.BooleanField(default=False) ##
    content = models.TextField() ##
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify_new(self.name, 4)
        return super().save(*args, **kwargs)


#7: Após criar o 'Category()' e 'CategoryAdmin()' você precisa realizar o makemigrations. Melhor rodar o comando 'docker compose up --build --force-recreate'.

# ------------------------------------------------------------------
#1: Se a pessoa não tiver enviado uma slug, vou gerar uma nova 'slug'.
#2: Esse campo é do tipo CharField, que armazena uma string com comprimento máximo de 15 caracteres. Este campo representará o nome da tag.
#3: Define um campo chamado slug no modelo Tag. Este campo é do tipo SlugField, que armazena strings "slugificadas" (normalmente usadas em URLs). O campo slug é configurado como único (unique=True), o que significa que cada slug deve ser único no banco de dados. Também permite valores None (com null=True) e valores em branco (com blank=True), com comprimento máximo de 255 caracteres.
#4: A condição if not self.slug verifica se o campo slug da instância do modelo Tag está vazio. Se estiver, ele entrará no bloco de código a seguir.
#5: A função slugify_new cria um "slug" a partir do name e adiciona 4 caracteres aleatórios ao final (detalhes dessa função estão explicados no módulo 'admin.py' do projeto).
#6:  Chama o método save() da classe pai (models.Model) para salvar a instância no banco de dados. O uso de super() garante que a implementação padrão do Django para salvar objetos seja executada.

# https://linktr.ee/edsoncopque