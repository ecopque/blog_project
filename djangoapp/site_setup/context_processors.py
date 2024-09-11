# FILE: /blog_project/djangoapp/site_setup/context_processors.py

from site_setup.models import SiteSetup

def context_processor_example(request):
    return {'example': 'EXAMPLE context_processors.py'} #4:

def site_setup(request):
    # IMPORT⬇: /blog_project/djangoapp/site_setup/models.py:
    setup = SiteSetup.objects.order_by('-id').first() #1:
    return {'site_setup': setup,} #5:
    # return {'site_setup': 'Hi, context_processor.py', 'title': 'Title', 'site_setup2': setup,} #2: #3:


# ------------------------------------------------------------------
#4: Esta função é um exemplo de context processor em Django. Ela retorna um dicionário contendo um par chave-valor que estará disponível em todos os templates da aplicação Django.
#5: Este é o retorno da função site_setup() e retorna um dicionário contendo o objeto setup, que foi definido na linha anterior. Este dicionário será disponibilizado em todos os templates da aplicação, possibilitando o acesso ao objeto site_setup nos templates para exibir ou utilizar as configurações do site.
# ------------------------------------------------------------------
#1: Recupera o primeiro registro do modelo SiteSetup, ordenado por ID decrescente (o mais recente primeiro).
#2: No dicionário retornado pela função site_setup, 'site_setup': 'Hi, context_processor.py' é apenas uma chave chamada 'site_setup' com um valor de string 'Hi, context_processor.py'. No contexto dos templates, você pode acessar isso usando a variável site_setup.
#3: Da mesma forma, 'title': 'Title' é uma chave chamada 'title' com um valor de string 'Title'. Isso pode ser acessado nos templates usando a variável title.

# https://linktr.ee/edsoncopque