# FILE: /blog_project/djangoapp/blog/urls.py

from django.urls import path
from blog.views import index, page, post, created_by, category

app_name = 'blog' #1:
# IMPORT⬇: /blog_project/djangoapp/blog/views.py
urlpatterns = [
    path('', index, name='index'), #2:
    path('page/<slug:slug>/', page, name='page'),
    path('post/<slug:slug>/', post, name='post'), #3:
    path('created_by/<int:author_pk>/', created_by, name='created_by'), ##
    path('category/<slug:slug>/', category, name='category'), ##
]



# ------------------------------------------------------------------
#3: Esta linha define uma rota na aplicação Django. Quando o usuário acessa uma URL que segue o padrão post/<slug:slug>/, a view post será chamada. O parâmetro slug na URL é passado para a view, e slug é um identificador amigável da URL (geralmente derivado do título do post).
# ------------------------------------------------------------------
#1: Esta linha define o namespace do aplicativo para o qual as URLs estão sendo configuradas. O Django permite agrupar as URLs de um aplicativo sob um namespace para evitar conflitos de nome com outras aplicações dentro do mesmo projeto. Nesse caso, o app_name é definido como 'blog', o que significa que todas as URLs definidas nesse arquivo serão referenciadas com o prefixo blog:. Por exemplo, a URL nomeada index será referenciada como blog:index.
#2: Esta linha define uma rota no Django. Aqui, a função path define o mapeamento entre a URL e a view correspondente. Esta rota é para a URL raiz (''), que significa que quando o usuário acessa a URL principal do aplicativo (sem nenhum caminho adicional), a view index será chamada. O argumento name='index' atribui um nome a essa URL, permitindo que ela seja referenciada de forma reversa no código e nos templates usando blog:index (devido ao app_name definido anteriormente).

# https://linktr.ee/edsoncopque