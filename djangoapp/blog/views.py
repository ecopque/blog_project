# FILE: /blog_project/djangoapp/blog/views.py

from django.shortcuts import render, redirect
from django.core.paginator import Paginator #3:
from blog.models import Post, Page
from django.db.models import Q #21:
from django.contrib.auth.models import User #26:
from django.http import Http404
from django.views.generic import ListView, DetailView #47:
from typing import Any
from django.db.models.query import QuerySet #48:

# posts = list(range(1000)) #4:
PER_PAGE = 9

class PostListView(ListView): #35:
    model = Post #36:
    template_name = 'blog/pages/index.html' #37:
    # EXPORT⬇: /blog_project/djangoapp/templates/blog/pages/index.html
    context_object_name = 'posts' #38:
    ordering = '-pk', #39:
    paginate_by = PER_PAGE #40:
    # queryset = Post.objects.get_published()

    def get_queryset(self): #41:
        queryset = super().get_queryset() #42:
        queryset = queryset.filter(is_published=True) #43:
        return queryset

    def get_context_data(self, **kwargs): #44:
        context = super().get_context_data(**kwargs) #45:
        context.update({'page_title': 'Home - ',}) #46:
        return context
    
#Substituído por 'class PostListView(ListView)':
# EXPORT⬇: /blog_project/djangoapp/blog/urls.py
# def index(request): #1:
#     # posts = Post.objects.filter(is_published=True).order_by('-pk') #12:
#     # IMPORT⬇: /blog/project/djangoapp/blog/models.py
#     posts = Post.objects.get_published() #13:
#     paginator = Paginator(posts, PER_PAGE) #5: #6!:
#     # URL⬇: http://127.0.0.1:8000/?page=1
#     page_number = request.GET.get("page") #7: #9:
#     page_obj = paginator.get_page(page_number) #8:
#     # IMPORT⬇: /blog_project/djangoapp/templates/blog/pages/index.html
#     return render(request, 'blog/pages/index.html', {'page_obj':page_obj, 'page_title': 'Home - '}) #2: #10: #27:

class CreatedByListView(PostListView): #49:
    def __init__(self, **kwargs: Any) -> None: #50:
        super().__init__(**kwargs)
    
    def get_context_data(self, **kwargs): #51:
        ctx = super().get_context_data(**kwargs) #52:
        author_pk = self.kwargs.get('author_pk') #53:
        user = User.objects.filter(pk=author_pk).first() #54:

        if user is None:
            raise Http404()
        
        user_full_name = user.username #55:
        if user.first_name:
            user_full_name = f'{user.first_name} {user.last_name}'
        
        page_title = 'Posts by ' + user_full_name + ' - ' #56:
        ctx.update({'page_title': page_title,}) #57:
        return ctx
    
    def get_queryset(self) -> QuerySet[Any]: #58:
        qs = super().get_queryset()
        qs = qs.filter(created_by__pk=self.kwargs.get('author_pk')) #59:
        return qs
    
    def get(self, request, *args, **kwargs): #60:
        author_pk = self.kwargs.get('author_pk') #61:
        user = User.objects.filter(pk=author_pk).first() #62:
        if user is None:
            return redirect('blog:index')
        return super().get(request, *args, **kwargs)

# Substituído por 'CreatedByListView(PostListView)':
# def created_by(request, author_pk):
#     user = User.objects.filter(pk=author_pk).first() #28:
#     if user is None: #29:
#         raise Http404() #30:
    
#     posts = Post.objects.get_published().filter(created_by__pk=author_pk) #18:
    
#     user_full_name = user.username
#     if user.first_name:
#         user_full_name = f'{user.first_name} {user.last_name}' #31:
    
#     page_title = 'Posts by ' + user_full_name + ' - ' #32:
#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#     return render(request, 'blog/pages/index.html', {'page_obj':page_obj, 'page_title': page_title,}) #33:

class CategoryListView(PostListView): #64:
    allow_empty = False #63:

    def get_queryset(self) -> QuerySet[Any]: #65:
        return super().get_queryset().filter(category__slug=self.kwargs.get('slug')) #66:
    
    def get_context_data(self, **kwargs): #67:
        ctx = super().get_context_data(**kwargs) #68:
        page_title = f'{self.object_list[0].category.name} - Category - ' #69:
        ctx.update({'page_title':page_title,})
        return ctx
    
# Substituído por 'CategoryListView(PostListView)':
# def category(request, slug):
#     posts = Post.objects.get_published().filter(category__slug=slug) #15: #19:

#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     if len(posts) == 0:
#         raise Http404()
#     page_title = f'{page_obj[0].category.name} Category - ' #34:
#     return render(request, 'blog/pages/index.html', {'page_obj':page_obj, 'page_title': page_title,})

class TagListView(PostListView):
    allow_empty = False

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset().filter(tags__slug=self.kwargs.get('slug'))
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        tag_slug = self.kwargs.get('slug') #70:
        tag_name = self.object_list[0].tags.filter(slug=tag_slug).first() #71:
        page_title = f'{tag_name} Tag - '
        ctx.update({'page_title':page_title,})
        return ctx

# Substituído por 'TagListView(PostListView)':
# def tag(request, slug):
#     # IMPORT⬇: /blog/project/djangoapp/blog/models.py
#     posts = Post.objects.get_published().filter(tags__slug=slug) #20:
#     paginator = Paginator(posts, PER_PAGE)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)

#     if len(page_obj) == 0:
#         raise Http404
#     page_title = f'{page_obj[0].tags.first().name} - Tags - '
#     return render(request, 'blog/pages/index.html', {'page_obj':page_obj, 'page_title':page_title,})

class SearchListView(PostListView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._search_value = '' #72:
    
    def setup(self, request, *args, **kwargs): #73:
        self._search_value = request.GET.get('search', '').strip() #73:
        return super().setup(request, *args, **kwargs) #73:

    def get_queryset(self) -> QuerySet[Any]: #74:
        search_value = self._search_value
        return super().get_queryset().filter(Q(title__icontains=search_value) | Q(excerpt__icontains=search_value) | Q(content__icontains=search_value))[0:PER_PAGE] #74:
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs) #75:
        search_value = self._search_value
        page_title = f'{search_value[:30]} - Search - ', #75:
        ctx.update({'page_title':page_title, 'search_value':search_value,}) #75:
        return ctx
    
    def get(self, request, *args, **kwargs): #76:
        if self._search_value == '': #76:
            return redirect('blog:index')
        return super().get(request, *args, **kwargs) #76:

# Substituído por 'SearchListView(PostListView)':
# def search(request):
#     # IMPORT⬇: /blog/project/djangoapp/blog/models.py
#     search_value = request.GET.get('search', '').strip() #22:
#     posts = Post.objects.get_published().filter(Q(title__icontains=search_value) | Q(excerpt__icontains=search_value) | Q(content__icontains=search_value))[0:PER_PAGE] #23:

#     page_title = f'{search_value[:30]} - Search - '
#     return render(request, 'blog/pages/index.html', {'page_obj':posts, 'search_value':search_value, 'page_title':page_title,}) #24:

class PageDetailView(DetailView): #77:
    model = Page #78:
    template_name = 'blog/pages/page.html' #79:
    slug_field = 'slug' #80:
    context_object_name = 'page' #81:

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]: #82:
        ctx = super().get_context_data(**kwargs) #83:
        page = self.get_object() #84:
        page_title = f'{page.title} - Page -' #85:
        ctx.update({'page_title':page_title,}) #86:
        return ctx
    
    def get_queryset(self) -> QuerySet[Any]: #87:
        return super().get_queryset().filter(is_published=True) #88:

# Substituído por 'PageDetailView(DetailView)':
# def page(request, slug):
#     page_obj = (Page.objects.filter(is_published=True).filter(slug=slug).first())

#     if page_obj is None:
#         raise Http404
#     page_title = f'{page_obj.title} - Page - '
#     return render(request,'blog/pages/page.html',{'page': page_obj, 'page_title': page_title}) #25:

# Antigo removido (page(request, slug):
# def page(request, slug): # Original
#     # paginator = Paginator(posts, 9)
#     # page_number = request.GET.get("page")
#     # page_obj = paginator.get_page(page_number)
#     # IMPORT⬇: /blog_project/djangoapp/templates/blog/pages/page.html
#     return render(request, 'blog/pages/page.html', {}) #11:

def post(request, slug): #14:
    post_obj = (Post.objects.get_published().filter(slug=slug).first()) #16:
    # paginator = Paginator(posts, 9)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)
    # IMPORT⬇: /blog_project/djangoapp/templates/blog/pages/post.html
    if post_obj is None:
        raise Http404
    page_title = f'{post_obj.title} - Post - '
    return render(request, 'blog/pages/post.html', {'post':post_obj, 'page_title': page_title,}) #17:

#77: Esta linha define a classe PageDetailView, que herda de DetailView. A DetailView é uma view genérica do Django usada para exibir os detalhes de uma única instância de um modelo.
#78: Especifica que o modelo associado a esta view é Page. Esse modelo está definido em /blog_project/djangoapp/blog/models.py e é utilizado para buscar os dados de uma página específica no banco de dados.
#79: Define o template que será utilizado para renderizar a página.
#80: Informa que o campo slug do modelo Page será usado para buscar a instância da página. O slug é uma string amigável para URLs que identifica unicamente a página.
#81: Especifica o nome que o objeto Page terá dentro do template. No template, o objeto poderá ser acessado como page.
#82: Esta função sobrescreve o método get_context_data da classe DetailView. Ela permite adicionar ou modificar os dados de contexto que são passados ao template. O método aceita kwargs como argumentos extras e retorna um dicionário de contexto.
#83: Chama o método get_context_data da superclasse (DetailView) para obter o contexto padrão, e atribui esse contexto à variável ctx.
#84: Usa o método get_object para obter a instância do modelo Page que está sendo visualizada. Essa instância é armazenada na variável page.
#85: Cria o título da página a ser exibido no template, concatenando o título da página obtida (page.title) com o texto - Page -.
#86: Atualiza o contexto (ctx) adicionando o page_title ao dicionário de contexto que será passado para o template.
#87: Esta função sobrescreve o método get_queryset da DetailView. Ele é responsável por definir o conjunto de dados (queryset) que será utilizado na view.
#88: Chama o get_queryset da superclasse (DetailView) para obter o conjunto de dados padrão e, em seguida, aplica um filtro para exibir apenas as páginas que estão publicadas (is_published=True).
# ------------------------------------------------------------------
#72: Esse valor será usado posteriormente para armazenar o valor da pesquisa inserida pelo usuário.
#73: Aqui, o método setup da SearchListView é responsável por inicializar o valor de _search_value com o parâmetro search obtido da URL (query string) via request.GET.get('search', ''). Ele utiliza .strip() para remover espaços em branco no início e no fim da string. Após isso, o método setup da classe-pai é chamado.
#74: Este é o método get_queryset, que filtra os objetos Post de acordo com o valor de pesquisa armazenado em _search_value. Ele utiliza a função Q do Django (from django.db.models import Q, linha 21) para realizar uma busca em múltiplos campos (title, excerpt, content) usando icontains, que executa uma pesquisa insensível a maiúsculas/minúsculas. O filtro aplica a limitação de resultados com PER_PAGE.
#75: Esse método get_context_data atualiza o contexto que será passado para o template. Ele define page_title como os primeiros 30 caracteres da string de pesquisa (search_value[:30]) e a string "Search", e então adiciona esse valor ao contexto, junto com search_value. Isso é feito para que esses valores possam ser exibidos no template.
#76: No método get, a lógica verifica se _search_value está vazio. Se estiver, o usuário é redirecionado para a página principal (blog:index). Caso contrário, o método get da classe-pai é chamado para processar normalmente a requisição.
# ------------------------------------------------------------------
#68: Aqui, estamos herdando o contexto do método get_context_data da classe pai (PostListView). Isso significa que estamos pegando todas as informações que já foram adicionadas ao contexto e adicionando mais algumas.
#69: Estamos criando um título para a página, usando a categoria do primeiro post da lista. A ideia é mostrar o nome da categoria no título da página.
#70: Estamos pegando o slug (identificador único) da tag da URL e armazenando em tag_slug.
#71: Buscamos o nome da tag correspondente ao slug que pegamos anteriormente. Assumimos que o primeiro post da lista (índice 0) tem a tag que estamos procurando.
# ------------------------------------------------------------------
#63: Se estiver como True, receberemos a mensagem de 'Nothing found'. Se estiver False, receberemos erro 404. Mas se estiver como True, deu erro. Imbecil.
#64: Essa classe é responsável por exibir uma lista de posts que pertencem a uma determinada categoria.
#65: Sobrescreve o método get_queryset() da classe base PostListView para filtrar os posts.
#66: Filtra os posts da categoria atual utilizando o slug (identificador único) da categoria que foi passado na URL. O slug é obtido através de self.kwargs.get('slug').
#67: Sobrescreve o método get_context_data() para adicionar o nome da categoria ao contexto que será passado para o template.
# ------------------------------------------------------------------
#47: ListView é uma classe genérica baseada em views do Django, usada para exibir listas de objetos de um modelo. Ela facilita a exibição de dados sem a necessidade de escrever código repetitivo para consultas no banco de dados, renderização de templates, etc.
#48:  QuerySet é um objeto que representa uma coleção de objetos do banco de dados que podem ser filtrados, ordenados e manipulados. É o tipo retornado quando se faz consultas no banco de dados através de métodos como filter(), get(), etc.
#49: CreatedByListView herda de PostListView e serve para listar posts de um autor específico. Essa classe especializa a lógica de listagem, adicionando um filtro para mostrar apenas os posts criados por um autor em particular.
#50: O método construtor __init__ inicializa a instância da classe CreatedByListView com os argumentos fornecidos (**kwargs). Ele chama o construtor da classe pai super().__init__(**kwargs) para garantir que a classe base (PostListView) seja devidamente inicializada.
#51: Esse método adiciona dados adicionais ao contexto que será passado para o template. Aqui ele é sobrescrito para incluir um título de página personalizado.
#52: Esse trecho chama o método da classe pai get_context_data para obter o contexto padrão (ex.: lista de posts), e depois adiciona mais dados a esse contexto.
#53: Extrai o valor de author_pk dos parâmetros da URL, que corresponde ao ID do autor cujos posts estão sendo listados.
#54: Faz uma consulta no modelo User para encontrar o usuário correspondente ao ID author_pk. O método first() retorna o primeiro resultado encontrado ou None se nenhum for encontrado.
#55: Se o usuário for encontrado, define o nome de exibição do autor com o valor do username do objeto User. Se o usuário tiver um nome e sobrenome, eles serão usados para formar o nome completo.
#56: Define o título da página concatenando uma string com o nome completo do autor, formatando a frase: "Posts by [Nome do Autor] - ".
#57: Atualiza o contexto passado para o template, adicionando o título da página (variável page_title) ao dicionário de contexto.
#58: Esse método retorna o conjunto de dados que será exibido. Aqui ele é sobrescrito para filtrar os posts por autor (author_pk).
#59: Filtra o conjunto de posts retornado para incluir apenas aqueles criados pelo autor cujo author_pk foi passado na URL.
#60: O método get é chamado quando uma requisição GET é feita para esta view. Ele substitui o método get padrão da classe ListView para adicionar lógica de verificação do autor antes de renderizar a página.
#61: Aqui, o método obtém o valor de author_pk a partir dos parâmetros passados na URL, que é armazenado em self.kwargs. kwargs contém os argumentos de keyword (como author_pk) que são passados quando a view é chamada. Neste caso, o ID do autor é extraído da URL.
#62: Uma consulta ao banco de dados é realizada no modelo User, filtrando o usuário com o pk (primary key) igual ao author_pk obtido da URL. O método first() retorna o primeiro usuário encontrado ou None se nenhum usuário com esse ID for encontrado. O resultado é atribuído à variável user.
# ------------------------------------------------------------------
#35: ListView é uma classe de view genérica no Django que exibe uma lista de objetos. Ela simplifica o processo de exibição de listas de modelos do banco de dados, sem a necessidade de escrever o código de consulta manualmente. PostListView é uma subclasse da classe ListView, que herda sua funcionalidade. Esta view será usada para exibir uma lista de objetos Post. Ao ser acessada na URL, será automaticamente processada e renderizada pelo Django com base no template e no modelo fornecidos.
#36: A view PostListView está associada ao modelo Post, o que significa que ela exibirá uma lista de objetos do tipo Post a partir do banco de dados.
#37: Esta linha especifica o template HTML que será usado para renderizar a lista de posts.
#38: Esta linha define o nome da variável de contexto que será passada ao template. No template, a lista de posts estará disponível como posts.
#39: Define a ordem dos objetos Post a serem exibidos. Aqui, os posts são ordenados de forma decrescente pelo campo pk (chave primária). O sinal de menos - indica que a ordenação será decrescente.
#40: Esta linha ativa a paginação dos resultados, limitando o número de objetos por página. A constante PER_PAGE foi definida como 9, o que significa que a cada página serão exibidos 9 posts.
#41: o: Esta função é sobrescrita para personalizar o conjunto de consultas (queryset) retornado pela view. Aqui, ela retorna apenas os posts que estão publicados.
#42: Chama o método get_queryset da superclasse ListView, que busca todos os objetos Post no banco de dados. Esse conjunto de resultados será modificado mais à frente no método.
#43: Aplica um filtro no queryset, retornando apenas os posts que têm o campo is_published definido como True, ou seja, posts que estão publicados.
#44: Esta função sobrescreve o método get_context_data da classe ListView. Ela é usada para adicionar dados adicionais ao contexto que será passado ao template. Nesse caso, dados como o título da página serão adicionados.
#45: Esta linha chama o método get_context_data da superclasse para obter o contexto padrão que a ListView já fornece, como a lista de posts.
#46: Atualiza o contexto com uma nova chave page_title, que contém o valor 'Home - '. Esse valor será utilizado no template para exibir o título da página.
# ------------------------------------------------------------------
#26: O modelo User é usado para representar usuários no sistema de autenticação do Django.
#27: Este comando utiliza o método render() do Django para renderizar a página HTML index.html, passando como contexto os objetos page_obj e page_title.
#28: Aqui, o sistema está filtrando o modelo User para encontrar o usuário com o primary key (chave primária) igual a author_pk. O método first() retorna o primeiro resultado encontrado ou None se não houver correspondência.
#29: Verifica se o usuário encontrado no código anterior é None, ou seja, se não existe um usuário com o primary key fornecido.
#30: Levanta uma exceção Http404, indicando que o recurso solicitado não foi encontrado, resultando na página "404 Not Found".
#31: Se o first_name do usuário estiver preenchido, concatena first_name e last_name para formar o nome completo do usuário.
#32: Gera um título de página dinâmico com base no nome completo do usuário, como Posts by John Doe - .
#33: Renderiza o template index.html e passa o contexto contendo page_obj e o título dinâmico page_title.
#34: Gera o título da página com base no nome da categoria do primeiro post (page_obj[0]) encontrado. Este título será algo como Technology Category - .
# ------------------------------------------------------------------
#25: Essa linha faz o render da página usando o template page.html, passando o objeto page para o contexto. O template page.html vai exibir os dados da página (como title e content), usando o objeto page.
# ------------------------------------------------------------------
#21: O Q é um módulo de Django que permite construir consultas complexas no banco de dados com operadores lógicos como OR (|) e AND (&). Ao utilizar o Q, você pode criar consultas dinâmicas que permitem combinar diferentes filtros de busca.
#22: Esta linha pega o valor da string passada na URL através do parâmetro search (/search/?search=valor). O método GET.get('search', '') recupera o valor de busca inserido pelo usuário, ou retorna uma string vazia se o valor não for encontrado. O método .strip() remove quaisquer espaços em branco no início ou no final da string.
#23: Aqui, a busca é realizada nos objetos Post. O método get_published() filtra apenas os posts publicados. Em seguida, o método filter() aplica uma pesquisa baseada no valor de search_value. Usando o Q, a busca procura posts cujo título (title), resumo (excerpt), ou conteúdo (content) contenham o valor de busca (icontains indica que a busca é insensível a maiúsculas e minúsculas). O resultado é então limitado aos primeiros 9 posts (0:PER_PAGE).
#24: Esta linha renderiza o template 'blog/pages/index.html' e passa dois parâmetros para o template: posts, contendo os resultados da busca, e search_value, contendo o termo que foi buscado. Estes dados serão utilizados na interface do usuário para exibir os posts e mostrar o valor de busca no campo de pesquisa.
# ------------------------------------------------------------------
#20: Essa linha filtra os posts que têm a tag com o slug fornecido na URL. O método filter(tags__slug=slug) procura por posts que possuem a tag com o slug especificado. A função get_published() faz parte do modelo Post e retorna apenas os posts que estão publicados.
# ------------------------------------------------------------------
#14: Adicionamos o slug, que não tinha antes. Agora o post está funcionando (ex: http://127.0.0.1:8000/post/eneas-carneiro-d6cn/).
#15: 'category__slug' significa que estamos buscando o campo 'slug' da foreingkey 'category'.
#16: Essa linha está buscando um post específico no banco de dados que corresponde ao slug fornecido. A função get_published() é um método personalizado no modelo Post (provavelmente em /blog/models.py), que retorna apenas posts que estão publicados. A função filter(slug=slug) restringe os resultados ao post cujo slug (parte da URL que identifica o post) corresponde ao valor passado pela URL. O first() retorna o primeiro objeto encontrado (ou None se nenhum for encontrado).
#17: O dicionário {'post': post} passa o post encontrado para o template, onde ele será usado para exibir detalhes específicos do post.
#18: Esta linha busca todos os posts publicados no banco de dados que foram criados por um autor específico. O filtro created_by__pk=author_pk utiliza a chave primária do autor (author_pk), que vem da URL, para selecionar os posts escritos por esse autor. A função get_published() retorna apenas os posts que estão publicados.
#19: Essa linha busca todos os posts publicados que pertencem a uma categoria específica. O filtro category__slug=slug utiliza o slug da categoria, passado na URL, para selecionar os posts que estão associados a essa categoria. O get_published() retorna apenas os posts que estão publicados, provavelmente definidos no modelo Post.
# ------------------------------------------------------------------
#13: Esta linha na função index chama o método get_published() definido na classe PostManager. Isso faz com que sejam recuperados do banco de dados apenas os posts que estão com o campo is_published=True e os ordena pela chave primária em ordem decrescente. O resultado será passado para o paginador logo abaixo.
# ------------------------------------------------------------------
#12: Esta linha está buscando todos os objetos do modelo Post (definido no módulo blog.models), filtrando-os para retornar apenas os que estão com a flag is_published=True. Ou seja, apenas os posts publicados serão incluídos. Em seguida, os resultados são ordenados pela chave primária (pk) em ordem decrescente ('-pk').
# ------------------------------------------------------------------
#3: A classe Paginator é usada para dividir um conjunto de dados em páginas menores e gerenciáveis. Neste código, Paginator é utilizado para paginar a lista de posts no blog.
#4: Define uma lista chamada posts que contém 1000 números (de 0 a 999). Este é um exemplo de lista de objetos que será paginada usando a classe Paginator.
#5: Cria uma instância de Paginator, passando dois argumentos: posts (a lista a ser paginada) e 9 (o número de itens por página). Isso divide a lista de posts em páginas de 9 itens cada.
#6: Foi dito que o segundo argumento é o número de posts por página. Em meus testes, mudando o número não houve diferença alguma. Mas veja no 'index.html', lá você consegue definir o número de posts por página.
#7: Obtém o número da página da requisição HTTP GET. 'request.GET.get("page")' extrai o parâmetro de query page da URL, que indica qual página deve ser exibida. Se o parâmetro não for passado na URL, o valor será None. Se o parâmetro "page" estiver presente na URL, ele retornará o valor dele; caso contrário, retornará None.
#8: Utiliza o método get_page() do Paginator para obter o objeto da página correspondente ao número da página (page_number). Se page_number for None ou inválido, ele retornará a primeira página.
#9: Exemplo: http://127.0.0.1:8000/?page=1.
#10: O terceiro argumento é um dicionário que representa o contexto a ser passado para o template. page_obj é um objeto retornado pelo método 'paginator.get_page(page_number)'.
#11: Renderiza o template page.html (importado de /blog_project/djangoapp/templates/blog/pages/page.html) passando um contexto vazio {}.
# ------------------------------------------------------------------
#1: Esta linha define uma função chamada index que recebe um parâmetro request. No Django, uma view (como essa) é uma função que recebe um pedido HTTP (request) e retorna uma resposta HTTP. Aqui, a função index será usada para processar o pedido quando o usuário acessa a URL associada a esta view.
#2: Esta linha utiliza a função render do Django para gerar uma resposta HTTP. A função render pega três parâmetros: o objeto request, o caminho para o template HTML que será renderizado ('blog/pages/index.html'), e opcionalmente um dicionário de contexto que pode ser passado para o template. O template 'blog/pages/index.html' será importado e renderizado como resposta quando a view index for chamada. Esse template está localizado no diretório /blog_project/djangoapp/templates/blog/pages/index.html.

# https://linktr.ee/edsoncopque