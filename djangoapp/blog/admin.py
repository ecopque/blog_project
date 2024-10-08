# FILE: /blog/project/djangoapp/blog/admin.py

from django.contrib import admin
from blog.models import Tag, Category, Page, Post
from django_summernote.admin import SummernoteModelAdmin #23:
from django.urls import reverse #29:
from django.utils.safestring import mark_safe #30:

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
# class PageAdmin(admin.ModelAdmin): #9:
class PageAdmin(SummernoteModelAdmin): #24:
    # URL⬇: http://127.0.0.1:8000/admin/blog/page/

    # IMPORT⬇: /blog/project/djangoapp/blog/models.py
    summernote_fields = ('content',) #25:

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
# class PostAdmin(admin.ModelAdmin):
class PostAdmin(SummernoteModelAdmin): #26:
    # URL⬇: http://127.0.0.1:8000/admin/blog/post/

    # IMPORT⬇: /blog/project/djangoapp/blog/models.py
    summernote_fields = ('content',) #22:

    list_display = 'id', 'title', 'is_published', 'created_by',
    list_display_links = 'title',
    search_fields = 'id', 'slug', 'title', 'excerpt', 'content',
    list_per_page = 50
    list_filter = 'category', 'is_published', #11:
    list_editable = 'is_published', #12:
    ordering = '-id',
    # URL⬇: http://127.0.0.1:8000/admin/blog/post/add/
    readonly_fields = 'created_at', 'updated_at', 'created_by', 'updated_by', 'link', #13: #31:
    prepopulated_fields = {"slug": ('title',),} #14:
    autocomplete_fields = 'tags', 'category' #15:

    def link(self, obj): #31:
        if not obj.pk:
            return '-'
        
        # IMPORT⬇: /blog_project/djangoapp/blog/urls.py
        url_post = reverse('blog:post', args=(obj.slug,)) #27: #32:
        safe_link = mark_safe(f'<a target="_blank" href="{url_post}">View post</a>') #28: #33:
        return  safe_link

    # IMPORT⬇: /blog/project/djangoapp/blog/models.py
    def save_model(self, request, obj, form, change): #16: #17:
        if change: #18:
            obj.updated_by = request.user #19:
        else:
            obj.created_by = request.user #20:
        obj.save() #21:



# ------------------------------------------------------------------
#27: BLOG: é a namespace da URL definida nas rotas (URLs) do Django. Ele faz parte do reverse('blog:post', ...), que indica que existe um app chamado 'blog' e que dentro dele há uma URL com o nome 'post'. POST: refere-se ao nome de uma rota específica dentro do app 'blog'. Geralmente, este nome de rota aponta para a view que renderiza uma página de um post específico. SLUG: faz parte da URL do post. No código args=(obj.slug,), o slug é passado como argumento, o que indica que ele é um identificador único utilizado para formar a URL de um post específico. O slug é geralmente uma string legível, derivada do título do post, usada para criar URLs amigáveis.
#28: Quando você for renderizar html no Django, você precisará informar que é seguro, ou seja, usar 'mark_safe'.
#29: O reverse é utilizado para gerar URLs dinâmicas baseadas em nomes de rotas. Neste código, ele será usado para construir o link para visualizar um post diretamente da página de administração.
#30: é uma função usada para marcar uma string como "segura" para renderização em HTML, ou seja, ela impede que o Django escape o HTML contido na string. Nesse caso, será utilizado para gerar um link HTML clicável no painel de administração.
#31: O 'link' dentro da variável é entendido como a função 'link', logo abaixo.
#32: Esta linha está utilizando a função reverse para gerar a URL de um post específico. O nome da rota 'blog:post' está sendo usado junto com o slug do objeto (obj) como argumento. O slug serve como identificador único do post na URL.
#33: Ele cria um link para o post gerado pela URL url_post e abre-o em uma nova aba (target="_blank").
# ------------------------------------------------------------------
#22: Este é o 'contente' do Post() de /blog/project/djangoapp/blog/models.py.
#23: Importa a classe SummernoteModelAdmin do pacote django_summernote, que é uma extensão da classe ModelAdmin do Django. Essa classe facilita a integração do editor Summernote nos campos de texto dos modelos administrados.
#24: A classe PageAdmin está sendo configurada para utilizar o editor de texto Summernote nos campos da página no Django admin. Ao herdar de SummernoteModelAdmin, ela habilita a edição de campos de texto longos (como o conteúdo da página) usando o Summernote.
#25: Aqui, o campo content do modelo Page será editável usando o editor Summernote no painel de administração do Django. Esta linha especifica que o campo content do modelo deve usar o editor de texto enriquecido.
#26: Assim como na classe PageAdmin, PostAdmin herda de SummernoteModelAdmin, tornando o editor Summernote disponível para os campos especificados dentro dessa classe.
# ------------------------------------------------------------------
#16: Com 'change', se estiver alterando será True. Se estiver criando, será False. Fique esperto!
#17: Esta linha define o método save_model dentro da classe PostAdmin, que herda de admin.ModelAdmin. O método save_model é um método especial utilizado no Django Admin para salvar um objeto no banco de dados. Ele é sobrescrito aqui para adicionar lógica customizada ao salvar um objeto Post. O método recebe quatro parâmetros: self: refere-se à instância da classe PostAdmin. request: o objeto de solicitação HTTP atual. obj: o objeto que está sendo salvo (neste caso, uma instância de Post). form: o formulário que está sendo submetido. change: um booleano que indica se o objeto está sendo criado (False) ou atualizado (True).
#18: Se change for True, significa que o objeto Post está sendo atualizado e não criado pela primeira vez. A lógica abaixo, então, executará o bloco de código correspondente para atualizar o campo updated_by.
#19: Se o objeto Post estiver sendo atualizado (quando change é True), esta linha define o campo updated_by do objeto Post como o usuário atual (request.user) que está fazendo a solicitação. Esse campo updated_by é uma ForeignKey para o modelo User (importado de django.contrib.auth.models no arquivo models.py) e armazena o usuário que fez a última atualização no objeto Post.
#20: Se o objeto Post está sendo criado pela primeira vez (quando change é False), esta linha define o campo created_by do objeto Post como o usuário atual (request.user). O campo created_by também é uma ForeignKey para o modelo User, e este campo armazenará o usuário que criou o objeto Post.
#21: Esta linha chama o método save() no objeto obj (a instância de Post que está sendo salva) para persistir as alterações no banco de dados. Este método é crucial porque, depois de definir quem criou ou atualizou o post, ele garante que essas informações sejam armazenadas no banco de dados.
# ------------------------------------------------------------------
#11: 'list_filter' é uma configuração da classe PostAdmin que define filtros no painel de administração do Django. Aqui, ele permite que o administrador filtre posts por category e is_published no painel de administração.
#12: Permite a edição direta de campos listados na visualização de lista do Django Admin. Aqui, o campo is_published pode ser editado diretamente da lista de posts.
#13: Define os campos que devem ser exibidos como somente leitura no formulário de administração do Django. Os campos created_at, updated_at, created_by, e updated_by são definidos como somente leitura para impedir alterações manuais.
#14: É uma configuração da classe PostAdmin que especifica que o campo slug será automaticamente preenchido com base no campo title ao adicionar ou editar um post no painel de administração.
#15: É uma configuração da classe PostAdmin que ativa o recurso de autocompletar para os campos tags e category no formulário de administração. Isso facilita a seleção de tags e categorias existentes.
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