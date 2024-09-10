# /blog_project/djangoapp/blog/views.py

from django.shortcuts import render

# EXPORT⬇: /blog_project/djangoapp/blog/urls.py
def index(request): #1:
    # IMPORT⬇: /blog_project/djangoapp/templates/blog/pages/index.html
    return render(request, 'blog/pages/index.html') #2:

def page(request):
    # IMPORT⬇: /blog_project/djangoapp/templates/blog/pages/page.html
    return render(request, 'blog/pages/page.html')

def post(request):
    # IMPORT⬇: /blog_project/djangoapp/templates/blog/pages/post.html
    return render(request, 'blog/pages/post.html')


# ------------------------------------------------------------------

#1: Esta linha define uma função chamada index que recebe um parâmetro request. No Django, uma view (como essa) é uma função que recebe um pedido HTTP (request) e retorna uma resposta HTTP. Aqui, a função index será usada para processar o pedido quando o usuário acessa a URL associada a esta view.
#2: Esta linha utiliza a função render do Django para gerar uma resposta HTTP. A função render pega três parâmetros: o objeto request, o caminho para o template HTML que será renderizado ('blog/pages/index.html'), e opcionalmente um dicionário de contexto que pode ser passado para o template. O template 'blog/pages/index.html' será importado e renderizado como resposta quando a view index for chamada. Esse template está localizado no diretório /blog_project/djangoapp/templates/blog/pages/index.html.