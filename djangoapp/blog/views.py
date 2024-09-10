# /blog_project/djangoapp/blog/views.py

from django.shortcuts import render

# EXPORT⬇: /blog_project/djangoapp/blog/urls.py
def index(request): ##
    # IMPORT⬇: /blog_project/djangoapp/templates/blog/pages/index.html
    return render(request, 'blog/pages/index.html') ##

def page(request):
    # IMPORT⬇: /blog_project/djangoapp/templates/blog/pages/page.html
    return render(request, 'blog/pages/page.html')

def post(request):
    # IMPORT⬇: /blog_project/djangoapp/templates/blog/pages/post.html
    return render(request, 'blog/pages/post.html')