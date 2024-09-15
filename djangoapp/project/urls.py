# FILE: /blog_project/project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('summernote/', include('django_summernote.urls')), #1:
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# ------------------------------------------------------------------
#1: Esta linha adiciona as URLs do pacote django-summernote ao projeto Django. Quando a URL /summernote/ for acessada, as URLs e as views fornecidas pelo django_summernote serão carregadas, permitindo a utilização do editor Summernote no site. Ela se conecta ao pacote django_summernote para manipular e exibir o editor de texto.

# https://linktr.ee/edsoncopque