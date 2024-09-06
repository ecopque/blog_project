# FILE: /blog_project/djangoapp/site_setup/context_processors.py

# LOCALE: /blog_project/djangoapp/site_setup/models.py
from site_setup.models import SiteSetup

def context_processor_example(request):
    return {'example': 'EXAMPLE context_processors.py'}

def site_setup(request):

    # LOCALE: /blog_project/djangoapp/site_setup/models.py:
    setup = SiteSetup.objects.order_by('-id').first()
    return {'site_setup': 'SITE_SETUP context_processors.py', 'title': 'Title', 'site_setup2': setup,}