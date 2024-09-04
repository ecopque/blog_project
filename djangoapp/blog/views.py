# /blog_project/djangoapp/blog/views.py

from django.shortcuts import render

def index(request):
    return render(request, 'blog/pages/index.html') # /blog_project/djangoapp/blog/urls.py