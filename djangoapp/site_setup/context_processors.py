# FILE: /blog_project/djangoapp/site_setup/context_processors.py

from site_setup.models import SiteSetup

def context_processor_example(request):
    return {'example': 'EXAMPLE context_processors.py'} ##

def site_setup(request):
    # IMPORT⬇: /blog_project/djangoapp/site_setup/models.py:
    setup = SiteSetup.objects.order_by('-id').first() #1: ##
    return {'site_setup': setup,}
    # return {'site_setup': 'Hi, context_processor.py', 'title': 'Title', 'site_setup2': setup,} #2: #3:


# ------------------------------------------------------------------
#1: Recupera o primeiro registro do modelo SiteSetup, ordenado por ID decrescente (o mais recente primeiro).
#2: No dicionário retornado pela função site_setup, 'site_setup': 'Hi, context_processor.py' é apenas uma chave chamada 'site_setup' com um valor de string 'Hi, context_processor.py'. No contexto dos templates, você pode acessar isso usando a variável site_setup.
#3: Da mesma forma, 'title': 'Title' é uma chave chamada 'title' com um valor de string 'Title'. Isso pode ser acessado nos templates usando a variável title.