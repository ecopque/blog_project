# FILE: /blog_project/djangoapp/blog/views.py

from django.shortcuts import render
from django.core.paginator import Paginator #3:
from blog.models import Post
from django.db.models import Q ##

# posts = list(range(1000)) #4:
PER_PAGE = 9

# EXPORT⬇: /blog_project/djangoapp/blog/urls.py
def index(request): #1:
    # posts = Post.objects.filter(is_published=True).order_by('-pk') #12:
    # IMPORT⬇: /blog/project/djangoapp/blog/models.py
    posts = Post.objects.get_published() #13:

    paginator = Paginator(posts, PER_PAGE) #5: #6!:
    # URL⬇: http://127.0.0.1:8000/?page=1
    page_number = request.GET.get("page") #7: #9:
    page_obj = paginator.get_page(page_number) #8:

    # IMPORT⬇: /blog_project/djangoapp/templates/blog/pages/index.html
    return render(request, 'blog/pages/index.html', {'page_obj':page_obj,}) #2: #10:

def page(request, slug):
    # paginator = Paginator(posts, 9)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)

    # IMPORT⬇: /blog_project/djangoapp/templates/blog/pages/page.html
    return render(request, 'blog/pages/page.html', {}) #11:

def post(request, slug): #14:
    post = (Post.objects.get_published().filter(slug=slug).first()) #16:
    # paginator = Paginator(posts, 9)
    # page_number = request.GET.get("page")
    # page_obj = paginator.get_page(page_number)

    # IMPORT⬇: /blog_project/djangoapp/templates/blog/pages/post.html
    return render(request, 'blog/pages/post.html', {'post':post,}) #17:

def created_by(request, author_pk):
    posts = Post.objects.get_published().filter(created_by__pk=author_pk) #18:
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/pages/index.html', {'page_obj':page_obj,})

def category(request, slug):
    posts = Post.objects.get_published().filter(category__slug=slug) #15: #19:
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/pages/index.html', {'page_obj':page_obj,})

def tag(request, slug):
    # IMPORT⬇: /blog/project/djangoapp/blog/models.py
    posts = Post.objects.get_published().filter(tags__slug=slug) #20:
    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/pages/index.html', {'page_obj':page_obj,})

def search(request):
    # IMPORT⬇: /blog/project/djangoapp/blog/models.py
    search_value = 'about' ##
    posts = Post.objects.get_published().filter(Q(title__icontains=search_value) | Q(excerpt__icontains=search_value) | Q(content__icontains=search_value))[0:PER_PAGE] ##

    return render(request, 'blog/pages/index.html', {'page_obj':posts,})

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
#7: Obtém o número da página da requisição HTTP GET. request.GET.get("page") extrai o parâmetro de query page da URL, que indica qual página deve ser exibida. Se o parâmetro não for passado na URL, o valor será None. Se o parâmetro "page" estiver presente na URL, ele retornará o valor dele; caso contrário, retornará None.
#8: Utiliza o método get_page() do Paginator para obter o objeto da página correspondente ao número da página (page_number). Se page_number for None ou inválido, ele retornará a primeira página.
#9: Exemplo: http://127.0.0.1:8000/?page=1.
#10: O terceiro argumento é um dicionário que representa o contexto a ser passado para o template. page_obj é um objeto retornado pelo método 'paginator.get_page(page_number)'.
#11: Renderiza o template page.html (importado de /blog_project/djangoapp/templates/blog/pages/page.html) passando um contexto vazio {}.
# ------------------------------------------------------------------
#1: Esta linha define uma função chamada index que recebe um parâmetro request. No Django, uma view (como essa) é uma função que recebe um pedido HTTP (request) e retorna uma resposta HTTP. Aqui, a função index será usada para processar o pedido quando o usuário acessa a URL associada a esta view.
#2: Esta linha utiliza a função render do Django para gerar uma resposta HTTP. A função render pega três parâmetros: o objeto request, o caminho para o template HTML que será renderizado ('blog/pages/index.html'), e opcionalmente um dicionário de contexto que pode ser passado para o template. O template 'blog/pages/index.html' será importado e renderizado como resposta quando a view index for chamada. Esse template está localizado no diretório /blog_project/djangoapp/templates/blog/pages/index.html.

# https://linktr.ee/edsoncopque