# /blog_project/djangoapp/blog/views.py

from django.shortcuts import render

# EXPORT⬇: /blog_project/djangoapp/blog/urls.py
def index(request): ##
    # IMPORT⬇: /blog_project/djangoapp/templates/blog/pages/index.html
    return render(request, 'blog/pages/index.html') ##