# FILE: /blog_project/djangoapp/blog/views.py

from django.shortcuts import render
from django.core.paginator import Paginator #3:

posts = list(range(1000)) #4:

# EXPORT⬇: /blog_project/djangoapp/blog/urls.py
def index(request): #1:
    paginator = Paginator(posts, 9) ##
    page_number = request.GET.get("page") ##
    page_obj = paginator.get_page(page_number) ##

    # IMPORT⬇: /blog_project/djangoapp/templates/blog/pages/index.html
    return render(request, 'blog/pages/index.html', {'page_obj': page_obj,}) #2: ##

def page(request):
    paginator = Paginator(posts, 9) ##
    page_number = request.GET.get("page") ##
    page_obj = paginator.get_page(page_number) ##

    # IMPORT⬇: /blog_project/djangoapp/templates/blog/pages/page.html
    return render(request, 'blog/pages/page.html', {}) ##

def post(request):
    paginator = Paginator(posts, 9) ##
    page_number = request.GET.get("page") ##
    page_obj = paginator.get_page(page_number) ##

    # IMPORT⬇: /blog_project/djangoapp/templates/blog/pages/post.html
    return render(request, 'blog/pages/post.html', {}) ##



#3: A classe Paginator é usada para dividir um conjunto de dados em páginas menores e gerenciáveis. Neste código, Paginator é utilizado para paginar a lista de posts no blog.
#4: Define uma lista chamada posts que contém 1000 números (de 0 a 999). Este é um exemplo de lista de objetos que será paginada usando a classe Paginator.



# ------------------------------------------------------------------

#1: Esta linha define uma função chamada index que recebe um parâmetro request. No Django, uma view (como essa) é uma função que recebe um pedido HTTP (request) e retorna uma resposta HTTP. Aqui, a função index será usada para processar o pedido quando o usuário acessa a URL associada a esta view.
#2: Esta linha utiliza a função render do Django para gerar uma resposta HTTP. A função render pega três parâmetros: o objeto request, o caminho para o template HTML que será renderizado ('blog/pages/index.html'), e opcionalmente um dicionário de contexto que pode ser passado para o template. O template 'blog/pages/index.html' será importado e renderizado como resposta quando a view index for chamada. Esse template está localizado no diretório /blog_project/djangoapp/templates/blog/pages/index.html.