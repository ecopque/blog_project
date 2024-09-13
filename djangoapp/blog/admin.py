# FILE: /blog/project/djangoapp/blog/admin.py

from django.contrib import admin
from blog.models import Tag, Category, Page, Post

# IMPORT⬇: /blog/project/djangoapp/blog/models.py
@admin.register(Tag) #3:
class TagAdmin(admin.ModelAdmin): #4:
    # URL⬇: http://127.0.0.1:8000/admin/blog/tag/
    list_display = 'id', 'name', 'slug', #2:
    list_display_links = 'id', 'name', #5:
    search_fields = 'id', 'name', 'slug', #6:
    list_per_page = 10 #7:
    ordering = '-id', #8:
    # URL⬇: http://127.0.0.1:8000/admin/blog/tag/add/
    prepopulated_fields = {"slug": ('name',),} #1:

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): #9:
    # URL⬇: http://127.0.0.1:8000/admin/blog/category/
    list_display = 'id', 'name', 'slug',
    list_display_links = 'name',
    search_fields = 'id', 'name', 'slug',
    list_per_page = 10
    ordering = '-id',
    # URL⬇: http://127.0.0.1:8000/admin/blog/category/add/
    prepopulated_fields = {"slug": ('name',),}

@admin.register(Page)
class PageAdmin(admin.ModelAdmin): #9:
    # URL⬇: http://127.0.0.1:8000/admin/blog/page/
    list_display = 'id', 'title', 'is_published',
    list_display_links = 'title',
    search_fields = 'id', 'slug', 'title', 'content',
    list_per_page = 50
    list_filter = 'is_published',
    list_editable = 'is_published', #10:
    ordering = '-id',
    # URL⬇: http://127.0.0.1:8000/admin/blog/page/add/
    prepopulated_fields = {"slug": ('title',),}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = 'id', 'title', 'is_published', 'created_by',
    list_display_links = 'title',
    search_fields = 'id', 'slug', 'title', 'excerpt', 'content',
    list_per_page = 50
    list_filter = 'category', 'is_published', #11: ##
    list_editable = 'is_published', #12: ##
    ordering = '-id',
    readonly_fields = 'created_at', 'updated_at', 'created_by', 'updated_by', #13: ##
    prepopulated_fields = {"slug": ('title',),} #14: ##
    autocomplete_fields = 'tags', 'category' #15: ##


    
# ------------------------------------------------------------------
#9: Após criar o 'Category()' e 'CategoryAdmin()' você precisa realizar o makemigrations. Melhor rodar o comando 'docker compose up --build --force-recreate'.
#10: O atributo list_editable na classe PageAdmin do Django Admin define quais campos na lista de objetos podem ser editados diretamente na interface de lista de objetos. Neste caso, o campo is_published da model Page pode ser editado diretamente. Facilita a administração de múltiplas páginas, permitindo que o administrador altere o status de publicação diretamente na lista sem precisar acessar cada objeto individualmente.
# ------------------------------------------------------------------
#1: Configura o campo slug para ser pré-preenchido (prepopulado) com base no valor do campo name na interface de administração do Django. Isso significa que, ao adicionar uma nova Tag através da interface de administração, o campo slug será automaticamente preenchido conforme o usuário digita o nome (name).
#2: Define os campos (id, name, slug) que serão exibidos na lista de objetos Tag na interface de administração. O campo id é o identificador padrão do Django para modelos, enquanto name e slug são os campos definidos no modelo Tag.
#3: Um decorator que registra o modelo Tag com o site de administração do Django.
#4: Essa classe configura a interface de administração do Django para o modelo Tag.
#5: Define quais campos (id, name) na lista de objetos Tag serão exibidos como links clicáveis, que levam à página de detalhes do objeto no admin.
#6: Define os campos (id, name, slug) que poderão ser pesquisados na interface de administração ao buscar por registros do modelo Tag.
#7: Define o número de objetos Tag que serão exibidos por página na interface de administração. Aqui, ele mostra 10 registros por página.
#8: Define a ordem de exibição dos objetos Tag na interface de administração. O -id indica que os objetos serão ordenados em ordem decrescente pelo campo id.

# https://linktr.ee/edsoncopque