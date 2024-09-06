# /blog_project/djangoapp/site_setup/context_processors.py

def context_processor_example(request): ##
    return {'example': 'EXAMPLE context_processors.py'} ##

def site_setup(request): ##
    return {'site_setup': 'SITE_SETUP context_processors.py', 'title': 'Title'} ##